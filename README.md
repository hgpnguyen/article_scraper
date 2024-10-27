<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
Currently, the scraper can only scrape "edition.cnn.com" and "vnexpress.net" domain website

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  python install -r requirements.txt
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/hgpnguyen/article_scraper.git
   ```
2. Setup virtual environment
    ```sh
    pip install virtualenv
    python3 -m venv <virtual-environment-name>
    source <virtual-environment-name>/bin/activate
    ```
3. Install requirement packages
  ```sh
  python install -r requirement.txt
  ```
4. Run web article_scraper
 ```sh
 python scrape_new.py <article-url>
 ```
 ### Example
  ```sh
 python scrape_new.py https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html
 ```
 ### Advance
 This is for anyone who want to run scraper with Splash to bypass restriction in some new websites
 1. Install Docker
 2. Pull the latest Splash image
 ```sh
 docker pull scrapinghub/splash
 ```
 3. Run container
```sh
 docker run -it -p 8050:8050 --rm scrapinghub/splash
```
4. Run spider
```sh
scrappy crawl article
```