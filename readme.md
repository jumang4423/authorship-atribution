## team k

s1270174 ryoma okuda

s1270203 Kenji Tsuda

s1270205 Shuto Hamaguchi

# = Authorship Attribution

## resolve dev dependencies

- general environment
  
  install python3 and make


- nix
```bash
# this reads shell.nix and resolves it
nix-shell
```


- docker
```bash
# this start a docker container
docker compose up -d
docker compose exec el331 bash

# if you want exit from docker... so
exit
# this code stop docker container (called el331) 
docker compose down
```

## program execution
- to test the coverage of predict correctness of the program
```bash
make install test
```


- to predict who write a given text by pipeline
```bash
cat datasets/test_data/AaronPressman/43033newsML.txt | make install run
```