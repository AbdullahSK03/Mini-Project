# Music.AI
A collaborative filtering based recommender system.

## Dataset links:👇👇👇👇

<br/>
https://drive.google.com/file/d/1GOCoJy9FsrCAxeMLjcstoWjA9UuJhSMS/view?usp=sharing

## Install all dependencies:
### Create virtual environment using the following command in terminal by opening the folder in terminal.
<code>pip install virtualenv</code>
<ul>
<!---->
<li><code>pip install streamlit</code></li>
<li><code>pip install scikit-learn</code></li>
<li><code>pip install pandas</code></li>
<li><code>pip install spotipy</code></li>
</ul>

## How to run:
<ol>
  <li>Download dataset from the link above</li>
  <li>Place the datasets (artists.csv & tracks.csv) in same folder where jupyter notebook is.</li>
  <li>Run the jupyter codes in jupyter notebook.</li>
  <li>After the code runs successfully you will see 2 new file i.e. similarity.pkl and df.pkl.</li>
  <li>
    Now open terminal in the for the folder where all files are located.
    Then run the following command in terminal
    <br/>
    <code>streamlit run main.py</code>
  </li>
</ol>

### OR
Run this command in terminal
<code>pip install -r Rrequirements.txt</code>

This command will read the <code>Requirements.txt</code> which contains all the required libraries.

## API keys

To get the Spotify API, you need to follow these steps:
<ol>
<li>Log into the dashboard using your Spotify account.(<a href='https://developer.spotify.com/dashboard'>Link</a>)</li>
<li>Create an app and get the app credentials (Client ID and Client Secret).</li>
<li>Request an access token using the app credentials1.</li>
<li>You can use your browser or a tool like Postman to make the requests.</li>
<li>For more detailed information, you can refer to the Spotify Web API documentation.</li>
</ol>


