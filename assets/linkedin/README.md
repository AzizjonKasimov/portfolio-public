# LinkedIn banner drafts

Flat-typography banner drafts for the LinkedIn profile, rendered locally with System.Drawing
(no screenshots, no private data, no generative-image output).

Run from PowerShell:

```powershell
.\assets\linkedin\render-banner.ps1
```

Output: `assets/linkedin/generated/linkedin-banner-a.png` at 1584 x 396 pixels (LinkedIn's
recommended banner size), the live banner since 2026-09-25. The unused draft B was removed on
2026-10-05; it is in git history. Text is kept out of the bottom-left corner, where the profile photo overlaps the banner.
The wording must stay aligned with `profile/linkedin.md` and the
facts in `experience/` and `community/`.
