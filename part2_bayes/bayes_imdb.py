# Part 2: Bayes' theorem on the IMDb reviews, basic Python only (csv and re).
# We work out P(Positive | keyword) = P(kw | Positive) * P(Positive) / P(kw)
import csv
import os
import re
import sys

DATA_PATH = "data/IMDB_Dataset.csv"

POSITIVE_KEYWORDS = ["superb", "outstanding", "wonderful", "excellent"]
NEGATIVE_KEYWORDS = ["worst", "waste", "awful", "terrible"]

WORD_RE = re.compile(r"[a-z']+")


def load_reviews(path=DATA_PATH):
    # returns a list of (set of words, sentiment), one entry per review
    # a set means a word is only counted once per review
    reviews = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            text = row["review"].lower().replace("<br />", " ")
            words = set(WORD_RE.findall(text))
            reviews.append((words, row["sentiment"].strip().lower()))
    return reviews


def count_stats(reviews, keywords):
    # counts how many reviews contain each keyword, and how many of those are positive
    n_total = len(reviews)
    n_pos = sum(1 for _, sentiment in reviews if sentiment == "positive")
    kw_total = {k: 0 for k in keywords}
    kw_pos = {k: 0 for k in keywords}
    for words, sentiment in reviews:
        for k in keywords:
            if k in words:
                kw_total[k] += 1
                if sentiment == "positive":
                    kw_pos[k] += 1
    return n_total, n_pos, kw_total, kw_pos


def bayes_posterior(prior, likelihood, marginal):
    # Bayes' theorem, this is the only place the formula is written
    if marginal == 0:
        raise ValueError("this keyword is not in any review, P(keyword) = 0")
    return likelihood * prior / marginal


def analyse(reviews, keywords):
    n_total, n_pos, kw_total, kw_pos = count_stats(reviews, keywords)
    prior = n_pos / n_total                       # P(Positive)
    results = []
    for k in keywords:
        likelihood = kw_pos[k] / n_pos            # P(kw | Positive)
        marginal = kw_total[k] / n_total          # P(kw)
        posterior = bayes_posterior(prior, likelihood, marginal)
        direct = kw_pos[k] / kw_total[k]          # same answer worked out from counts, to check
        results.append({"keyword": k, "count_pos": kw_pos[k], "count_all": kw_total[k],
                        "prior": prior, "likelihood": likelihood, "marginal": marginal,
                        "posterior": posterior, "direct": direct})
    return results


def print_table(title, results):
    print(f"\n{title}")
    print(f"{'keyword':<13}{'P(Pos)':>8}{'P(kw|Pos)':>11}{'P(kw)':>9}{'P(Pos|kw)':>11}{'check':>8}{'#reviews':>10}")
    print("-" * 70)
    for r in results:
        print(f"{r['keyword']:<13}{r['prior']:>8.4f}{r['likelihood']:>11.4f}"
              f"{r['marginal']:>9.4f}{r['posterior']:>11.4f}{r['direct']:>8.4f}{r['count_all']:>10}")


def markdown_table(results):
    lines = ["| Keyword | Prior P(Positive) | Likelihood P(kw\\|Positive) | Marginal P(kw) | Posterior P(Positive\\|kw) |",
             "|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['keyword']} | {r['prior']:.4f} | {r['likelihood']:.4f} | "
                     f"{r['marginal']:.4f} | {r['posterior']:.4f} |")
    return "\n".join(lines)


def main():
    # use the path typed in the command, or the default path
    path = sys.argv[1] if len(sys.argv) > 1 else DATA_PATH
    if not os.path.exists(path):
        print("Cannot find the file:", path)
        print("Put the CSV at that path, or run: python bayes_imdb.py path/to/file.csv")
        return
    reviews = load_reviews(path)
    print("Loaded", len(reviews), "reviews")
    print_table("Positive keywords", analyse(reviews, POSITIVE_KEYWORDS))
    print_table("Negative keywords", analyse(reviews, NEGATIVE_KEYWORDS))


if __name__ == "__main__":
    main()
