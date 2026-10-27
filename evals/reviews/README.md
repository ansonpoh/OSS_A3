# Independent AI reviews

Mock grading rounds on the repository. Each round used two independent AI graders, each with a clean clone and
the brief (`BRIEF.md`). Both were read-only and re-ran the offline checks, and each was told to verify every
claim against the brief.

- [round5.md](round5.md): graded at commit `8f98e93`. The response is in `b563cbd` and `f353fb2`.
- [round6.md](round6.md): graded at commit `67e7708`. The response is in `d017a23` and `d59b0aa`.

The summaries keep the scores, the top findings with the points each grader deducted, and the commits that
answered them. The full grading texts are not in the repository. The graders' work is not a substitute for the
owner's verdicts in `evals/golden/runs/*/review.md`.
