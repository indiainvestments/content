# r/IndiaInvestments Wiki

The source for **[www.indiainvestments.wiki](https://www.indiainvestments.wiki)** — a
community-written reference on investing, insurance, tax and personal finance in India,
grown out of posts on [r/IndiaInvestments](https://www.reddit.com/r/IndiaInvestments/).

This repository *is* the site. Pages are plain Markdown in `content/`; every push to
`main` rebuilds and republishes automatically via GitHub Actions. There is no CMS and
no separate publishing step.

## Found something wrong?

Every page on the site carries a **Fix this page** link that opens the right file in
GitHub's editor. Edit, commit, done — the correction is live in a couple of minutes.

For anything larger, or if you would rather just report it,
[open an issue](https://github.com/indiainvestments/content/issues/new).

## Editing and running it

See **[CONTRIBUTING-hugo.md](CONTRIBUTING-hugo.md)** — front matter reference, writing
conventions, and how the review-date system works.

```
content/          the pages — the tree mirrors the site's URLs exactly
.gitbook/assets/  images, served at /images/<filename>
layouts/          every template (no theme)
assets/           one plain-CSS stylesheet, one vanilla-JS file
scripts/          the CI checks
```

Running it locally is optional: `hugo server -D` with Hugo v0.158 or newer. No
`extended` build, no submodules, no npm, no Sass.

## A note on freshness

Indian tax law and regulation change every year, and this wiki was largely written in
2021. Every page shows when a human last *verified* it, and warns you when that was too
long ago. Treat any specific rate, limit or threshold as unverified until the banner
says otherwise, and check a primary source before acting on it.

Pages are classified by how fast they decay — `fast-rot` (rates, limits, platforms),
`slow-drift` (product structures), `evergreen` (principles and maths) — which sets how
often each needs re-checking. The annual pass happens in April, after the Finance Act
is enacted.

## License

Content is licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). It is
educational material, not financial advice — see
[the full disclaimers](https://www.indiainvestments.wiki/disclaimers-and-disclosures/).

## Contributors ✨

Our heartiest gratitude, to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://reddit.com/r/IndiaInvestments"><img src="https://avatars.githubusercontent.com/u/36945608?v=4?s=100" width="100px;" alt=""/><br /><sub><b>r/IndiaInvestments</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=indiainvestments" title="Documentation">📖</a> <a href="#infra-indiainvestments" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/indiainvestments/content/commits?author=indiainvestments" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Aindiainvestments" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-indiainvestments" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/financenoob"><img src="https://avatars.githubusercontent.com/u/78473984?v=4?s=100" width="100px;" alt=""/><br /><sub><b>financenoob</b></sub></a><br /><a href="#infra-financenoob" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/indiainvestments/content/commits?author=financenoob" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/commits?author=financenoob" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Afinancenoob" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-financenoob" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/Itsmarzil"><img src="https://avatars.githubusercontent.com/u/78316021?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marz</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=Itsmarzil" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3AItsmarzil" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-Itsmarzil" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/takeda-discord"><img src="https://avatars.githubusercontent.com/u/78316140?v=4?s=100" width="100px;" alt=""/><br /><sub><b>takeda-discord</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=takeda-discord" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/commits?author=takeda-discord" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Atakeda-discord" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-takeda-discord" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/Cephalopterus"><img src="https://avatars.githubusercontent.com/u/66165136?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Cephalopterus</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=Cephalopterus" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/commits?author=Cephalopterus" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3ACephalopterus" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-Cephalopterus" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/crimelabs786"><img src="https://avatars.githubusercontent.com/u/56079307?v=4?s=100" width="100px;" alt=""/><br /><sub><b>crimelabs786</b></sub></a><br /><a href="#infra-crimelabs786" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/indiainvestments/content/commits?author=crimelabs786" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/commits?author=crimelabs786" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Acrimelabs786" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-crimelabs786" title="Tutorials">✅</a> <a href="#question-crimelabs786" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/reo-sam"><img src="https://avatars.githubusercontent.com/u/36949552?v=4?s=100" width="100px;" alt=""/><br /><sub><b>reo-sam</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=reo-sam" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/commits?author=reo-sam" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Areo-sam" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-reo-sam" title="Tutorials">✅</a> <a href="#question-reo-sam" title="Answering Questions">💬</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/try2tame"><img src="https://avatars.githubusercontent.com/u/78716242?v=4?s=100" width="100px;" alt=""/><br /><sub><b>try2tame</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=try2tame" title="Documentation">📖</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Atry2tame" title="Reviewed Pull Requests">👀</a> <a href="#tutorial-try2tame" title="Tutorials">✅</a> <a href="#question-try2tame" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/LingeringDeep"><img src="https://avatars.githubusercontent.com/u/78742827?v=4?s=100" width="100px;" alt=""/><br /><sub><b>LingeringDeep</b></sub></a><br /><a href="#tutorial-LingeringDeep" title="Tutorials">✅</a> <a href="#question-LingeringDeep" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/I-am-Optimistic"><img src="https://avatars.githubusercontent.com/u/67626554?v=4?s=100" width="100px;" alt=""/><br /><sub><b>I-am-Optimistic</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=I-am-Optimistic" title="Documentation">📖</a> <a href="#tutorial-I-am-Optimistic" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/Tulip2MF"><img src="https://avatars.githubusercontent.com/u/78700380?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tulip2MF</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=Tulip2MF" title="Documentation">📖</a> <a href="#tutorial-Tulip2MF" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/villageindian"><img src="https://avatars.githubusercontent.com/u/78730706?v=4?s=100" width="100px;" alt=""/><br /><sub><b>villageindian</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=villageindian" title="Documentation">📖</a> <a href="#tutorial-villageindian" title="Tutorials">✅</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Avillageindian" title="Reviewed Pull Requests">👀</a> <a href="#question-villageindian" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/namasteOriginally"><img src="https://avatars.githubusercontent.com/u/78691162?v=4?s=100" width="100px;" alt=""/><br /><sub><b>namasteOriginally</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=namasteOriginally" title="Code">💻</a> <a href="#tutorial-namasteOriginally" title="Tutorials">✅</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3AnamasteOriginally" title="Reviewed Pull Requests">👀</a> <a href="#question-namasteOriginally" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/shryzel"><img src="https://avatars.githubusercontent.com/u/49168010?v=4?s=100" width="100px;" alt=""/><br /><sub><b>shryzel</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=shryzel" title="Documentation">📖</a> <a href="#tutorial-shryzel" title="Tutorials">✅</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Ashryzel" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/rajatdhoot123"><img src="https://avatars.githubusercontent.com/u/18528826?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rajat</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=rajatdhoot123" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Arajatdhoot123" title="Reviewed Pull Requests">👀</a> <a href="#question-rajatdhoot123" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://infilimits.com"><img src="https://avatars.githubusercontent.com/u/12628996?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shaswat Saxena</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=shaswatsaxena" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Ashaswatsaxena" title="Reviewed Pull Requests">👀</a> <a href="#question-shaswatsaxena" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/JimWithoutJam"><img src="https://avatars.githubusercontent.com/u/78673642?v=4?s=100" width="100px;" alt=""/><br /><sub><b>jimWithoutJam</b></sub></a><br /><a href="#infra-jimWithoutJam" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/indiainvestments/content/commits?author=jimWithoutJam" title="Code">💻</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3AjimWithoutJam" title="Reviewed Pull Requests">👀</a> <a href="#question-jimWithoutJam" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/VineetRDiscord"><img src="https://avatars.githubusercontent.com/u/48187416?v=4?s=100" width="100px;" alt=""/><br /><sub><b>VineetRDiscord</b></sub></a><br /><a href="#infra-VineetRDiscord" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#business-VineetRDiscord" title="Business development">💼</a> <a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3AVineetRDiscord" title="Reviewed Pull Requests">👀</a> <a href="#question-VineetRDiscord" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/M-e-r-c-u-r-y"><img src="https://avatars.githubusercontent.com/u/37909009?v=4?s=100" width="100px;" alt=""/><br /><sub><b>M-e-r-c-u-r-y</b></sub></a><br /><a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3AM-e-r-c-u-r-y" title="Reviewed Pull Requests">👀</a> <a href="#question-M-e-r-c-u-r-y" title="Answering Questions">💬</a> <a href="https://github.com/indiainvestments/content/commits?author=M-e-r-c-u-r-y" title="Documentation">📖</a></td>
    <td align="center"><a href="http://jtnydv.gitbook.io"><img src="https://avatars.githubusercontent.com/u/14368729?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jatin Yadav</b></sub></a><br /><a href="#infra-Jtnydv" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/indiainvestments/content/commits?author=Jtnydv" title="Code">💻</a> <a href="#question-Jtnydv" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/yashovardhan99/"><img src="https://avatars.githubusercontent.com/u/24536718?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yashovardhan Dhanania </b></sub></a><br /><a href="https://github.com/indiainvestments/content/pulls?q=is%3Apr+reviewed-by%3Ayashovardhan99" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://fully-faltoo.com/"><img src="https://avatars.githubusercontent.com/u/1546426?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Pratyush Mittal</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=pratyushmittal" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/webholik"><img src="https://avatars.githubusercontent.com/u/360759?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ankit Saini</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=webholik" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/arjitg"><img src="https://avatars.githubusercontent.com/u/15131095?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Arjit Gupta</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=arjitg" title="Documentation">📖</a></td>
    <td align="center"><a href="http://phalgun.in/"><img src="https://avatars.githubusercontent.com/u/915425?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Phalgun Guduthur</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=phalgun" title="Documentation">📖</a></td>
    <td align="center"><a href="https://shreyasgupta.in/"><img src="https://avatars.githubusercontent.com/u/20678047?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shreyas Gupta</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=sggts04" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/suhaga15"><img src="https://avatars.githubusercontent.com/u/22257346?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Suhag</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=suhaga15" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Uninspired-sapien"><img src="https://avatars.githubusercontent.com/u/102660286?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Uninspired-sapien</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=Uninspired-sapien" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/draco-malfoy"><img src="https://avatars.githubusercontent.com/u/46344490?v=4?s=100" width="100px;" alt=""/><br /><sub><b>draco-malfoy</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=draco-malfoy" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/srinivesh"><img src="https://avatars.githubusercontent.com/u/79801397?v=4?s=100" width="100px;" alt=""/><br /><sub><b>srinivesh</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=srinivesh" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/xero08"><img src="https://avatars.githubusercontent.com/u/856525?v=4?s=100" width="100px;" alt=""/><br /><sub><b>xero08</b></sub></a><br /><a href="https://github.com/indiainvestments/content/commits?author=xero08" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome! [Start here](contributors/)