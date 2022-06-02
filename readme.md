team k

==

s1270174 ryoma okuda

s1270203 Kenji Tsuda

s1270205 Shuto Hamaguchi

# = Authorship Attribution

## pusuedo

1. Download the dataset from the specified url.
2. The dataset has random texts written by 50 authors.
We need to select 10 authors
3. 10% of text is for text cases, another 90% is for training data.
Parse the word split by whitespace, and then count each word into python array of dictionary type.

4. Calculate the cosine similarity of test data and trained data using numpy(especially .dot and .norm functions)
5. The highest score of the cosine similarity will be the answer.

## resolve dev dependencies
### 1. to run this project, you need to install python3 and some dependencies.

- nix
```bash
# this reads shell.nix and resolves it
nix-shell
make install
```

- generic cli
  - install python3 and make. yes
  - ```make install```


- docker
```bash
docker compose up -d
docker compose exec el331 bash
make install
```

- if you want out, just enter:
```bash
exit
# this code stop docker container (called el331) 
docker compose down
```

### 2. excution or testing

- edit condig.yaml

- run test
```bash
make test
```