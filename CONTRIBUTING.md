# Contributing

This is a private research repository for the VDAC1 Gate-Opening Therapeutic Stack. When this repository goes public, contributions will be welcome under the following guidelines.

## How to Contribute

### Computational Contributions

- **GJS equation extensions**: New lock terms, sensitivity analyses, parameter sweeps
- **Simulation improvements**: Better visualization, additional pharmacology models
- **Literature mining**: Identifying relevant papers, particularly structural data on VDAC1 oligomerization or statin-mitochondria interactions

To contribute code:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-analysis`)
3. Commit with clear messages describing what the analysis shows
4. Open a pull request with context on how it relates to the GJS framework

### Experimental Proposals

If you have bench access and want to run one of the six defined experiments (or a related experiment):
1. Open an issue describing the proposed experiment
2. Include: cell line, reagents, readouts, timeline, and how results would feed back into the framework
3. Negative results are equally valuable -- they trigger the kill conditions that make this framework credible

### Literature and Evidence

- Corrections to cited references
- New publications relevant to VDAC1 oligomerization, statin-mitochondria biology, or MSS CRC immunotherapy
- Open an issue with the citation, DOI, and a brief note on relevance to the GJS framework

## Standards

- **No fabricated data.** All experimental results must come from actual bench work. Simulations must be clearly labeled as computational predictions.
- **Negative results welcome.** A kill condition triggered is a contribution to science, not a failure.
- **Cite properly.** Follow the reference organization in `references/README.md`.
- **Keep the root clean.** Scripts go in `simulations/`, figures in `figures/`, protocols in `experiments/`.

## Code Style

- Python scripts should include a header comment referencing the SAD section they support
- Use `matplotlib` with the serif typography settings established in `gjs_simulation.py`
- Output figures to `figures/` with descriptive filenames

## License

By contributing, you agree that your contributions will be licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).

## Contact

Anthony J. Vasquez Sr. -- Delaware Valley University
