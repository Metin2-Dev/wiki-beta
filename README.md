<!-- REPOSITORY -->
[repository:build]: https://github.com/Metin2-Dev/Metin2-Wiki-betadev/actions/workflows/build.yml/badge.svg
[repository:build-badge]: https://github.com/Metin2-Dev/Metin2-Wiki-betadev/actions/workflows/build.yml
[repository:contributing]: https://metin2-dev.github.io/wiki/pages/about/contributing

[stable-repository]: https://github.com/Metin2-Dev/Wiki


<!-- LINKS -->
[metin2dev:forum]: https://metin2.dev/



[![Build][repository:build]][repository:build-badge]

# Dev/Beta Wiki
A metin2 related Wiki with information about official content
and topics

This repository is just for development and beta preview
of content, for stable and latest content check the 
[stable repository][stable-repository]


## Developing

### Setup
 - Install [Python 3.10](https://www.python.org/downloads/release/python-3104/)
 - Clone this repository by typing `git clone https://github.com/OriDevTeam/Metin-Wiki`
 - Install **Pipenv** by typing `pip install pipenv` on your terminal
 - Install dependencies by typing `pip install`


## Building locally
 - Build by typing `pipenv run build`
 - Or by doing `cd docs/` and typing `make html`
 - Whenever you need to clean type `make clean`

**Note:** If you don't have `make` on Windows, you can use 
`make.bat` instead


## Previewing
To preview locally on the browser after building do
`make open` or open the html in `docs/_build/html/index.html`


## Contributing
If you wish to contribute to the project, be sure to read the 
[Contributing Guidelines][repository:contributing]



