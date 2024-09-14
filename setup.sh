mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"2018e143@eng.jfn.ac.lk\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml