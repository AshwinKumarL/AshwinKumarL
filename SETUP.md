# Setup — AshwinKumarL profile redesign

1. Create (or use) the public profile repository named exactly `AshwinKumarL/AshwinKumarL`.
2. Upload the contents of this package, preserving the `assets/` and `.github/workflows/` folders.
3. Commit and push the files to GitHub's default branch.
4. In the repository, open **Actions** and run **Generate contribution animation** once. Approve the workflow if GitHub asks.
5. Wait for the workflow to finish. It publishes `github-contribution-grid-snake-dark.svg` to the `output` branch. The README then displays it automatically.

## Important permissions

The workflow requests `contents: write` only so it can update the `output` branch. If your organization or repository restricts actions, enable workflow write permissions in **Settings → Actions → General → Workflow permissions**.

## Files included

- `README.md` — profile content and live stat cards.
- `assets/minecraft-header.gif` — animated purple/red Minecraft-inspired banner.
- `assets/minecraft-header.png` — high-resolution source still for the banner.
- `assets/achievements.svg` — lightweight animated achievement panel.
- `.github/workflows/profile-animations.yml` — daily real-contribution animation generator.

## Personalization

The profile username is already set to `AshwinKumarL`. Update only the text in `README.md` if your bio or achievement wording changes. Live statistic cards and the contribution animation update from GitHub rather than using invented counts.

## Note about animation

GitHub README files cannot run arbitrary JavaScript or custom CSS. The animations here are standard GIF/SVG images, and GitHub Actions refreshes the contribution animation from actual GitHub data.
