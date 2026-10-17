# markbeachill/tutorprompts

- 链接：https://github.com/markbeachill/tutorprompts
- 作者：markbeachill
- 仓库说明：AI Tutor prompts for students and tutors
- 星数：1
- 获取方式：GitHub README

---

## README

# AI Personal Tutor Toolkit

The AI Personal Tutor Toolkit is a set of prompt libraries that help students use AI as a tutor, not as a ghost-writer.

The prompts are designed to give structured, specialist writing support: focused feedback, plain explanation, practice and revision guidance while students keep responsibility for their own writing and thinking. The v4.4.1 release refreshes the website entry routes, Try It/download guidance and positive no-ghost-writing copy, while preserving the v4.4.0 in-tool help system and optional EAL mode.

Live website: https://markbeachill.github.io/tutorprompts/

## What the toolkit helps with

- Writing clarity, style and repeated mistakes.
- Paragraph and whole-draft structure.
- Academic argument, evidence and concept clarity.
- Research proposal development.
- Revision planning and AI-use records.

## How students use it

1. Open the live website.
2. Choose a toolkit file.
3. Upload or paste it into an AI tool.
4. Type `prompt`.
5. Choose the help they need.

The toolkit files are provided as plain Markdown prompt libraries because that makes them easy for AI tools to read. Students do not need to understand Markdown to use the toolkit.

## For educators

The toolkit offers a structured way to guide independent student AI use. It is not a replacement for assessment rules, teacher judgement, institutional policy or student responsibility.

Educators can inspect the prompts, test them, adapt them for local teaching contexts, and use the testing pack before recommending a version to students.

## Where are the prompt files?

The prompt libraries are stored inside the public site folder:

- `docs/prompt-libraries/latest/`

They live there because GitHub Pages publishes the website from `/docs`, and the live download links use those files directly.

For a developer-focused guide to the prompt files and build workflow, see `BUILD_AND_GENERATOR_GUIDE.md`.

## Customising the prompt libraries

The official mini libraries are recommended for most users. Developers, teachers and departments who want a smaller or locally tailored library can start from the master library and delete down.

See:

- `BUILD_AND_GENERATOR_GUIDE.md` — where the source and generated files live, and how to rebuild them
- `CUSTOMISING_PROMPTS.md` — how to build a smaller custom library without duplicating files or weakening the core tutor-not-ghost-writer design

## Repository structure

The public website is published from the `docs/` folder. Current maintainer documentation is kept separate from the public site.

```text
/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── BUILD_AND_GENERATOR_GUIDE.md
├── PACKAGE_GENERATOR_START_HERE.md
├── UPDATE-CHECKLISTS.md
├── CUSTOMISING_PROMPTS.md
├── SOURCE_MATERIAL_INDEX_EXPLAINER.md
├── src/
├── scripts/
├── docs/              # public GitHub Pages site
├── project-docs/      # current maintainer/developer docs
├── tool-history/      # past tool design decisions and release-era notes
└── roadmaps/          # future work and proposals
```

GitHub Pages can publish from the committed `docs/` folder, or from the optional GitHub Actions build workflow described in `BUILD_AND_GENERATOR_GUIDE.md`.

## For maintainers and AI assistants

If you are updating or rebuilding the repository without prior context:

1. Read `BUILD_AND_GENERATOR_GUIDE.md`.
2. Read `UPDATE-CHECKLISTS.md` and use the relevant checklist for the change.
3. Read `project-docs/README.md` and `project-docs/repository-layout.md`.
4. Edit source files under `src/` or generator files under `scripts/`.
5. Rebuild and check with `python scripts/run_generator_checks.py --build-first`.
6. Do not treat `tool-history/` or `roadmaps/` as current instructions unless the user explicitly asks you to implement something from them.

## Current public release

- Site package: v4.4.1
- Prompt-library suite: v4.4.1
- Testing/audit pack: v4.4.0

Detailed release notes are in `docs/changelog/site-update-notes/`.

## Discussion

Comments, questions and suggestions can be added in the repository discussions area:

https://github.com/markbeachill/tutorprompts/discussions


## Build instructions

See [`BUILD_AND_GENERATOR_GUIDE.md`](BUILD_AND_GENERATOR_GUIDE.md) for the consolidated library/page build workflow and release-version policy. Current maintainer details live in [`project-docs/`](project-docs/).

