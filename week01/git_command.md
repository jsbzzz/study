## git의 작동 방식
- ### 

## 기본적인 git 명령어
- ### git config
  - 사용자 정보 및 환경 설정
    - 기본적으로 지역(local), 전역(global), 시스템(system)설정으로 구분됨
    - 일반적으로 commit을 할 때 기록될 사용자 정보를 설정하거나
      ``` bash
      git config --global user.name "Alice" #전역으로 사용될 사용자 이름 설정
      git config --global user.email "alice123@gmail.com" # 전역으로 사용되 사용자 메일 설정
      ```
      자주 사용하는 명령어의 별칭을 정해 사용할 수 있다. 
      ``` bash
      git config --global alias.cl "config -l" #이후 git cl만 입력해도 git config -l과 같은 명령 실행
      ```
    - `git config --list` 를 이용해 설정 내용을 확인할 수 있다.

- ### git init
  - 현재 디렉터리를 git 저장소로 설정<br>
    `git init`<br>
    실행 시 해당 디렉터리에 .git 디렉터리가 숨김 상태로 생성됨

- ### git remote
  - 원격 저장소와 연결<br>
    ``` bash
    git remote add <저장소_이름> <url>
    ```
  - 저장된 원격 저장소를 확인할 때 사용 가능한 명령어
    ``` bash
    git remote # -v 옵션 사용시 주소도 확인 가능
    git remote show <저장소_이름> # 저장소의 자세한 정보 확인
    ```

- ### git clone
  - 원격 저장소를 통째로 가져와 추가
    ```bash
    git clone <url>
    ```
- ### git status
  - 저장소의 상태를 확인하는 명령어
    ```bash
    git status
    ```

- ### git add
  - 파일이나 디렉터리를 Staging Area에 추가. Staging Area에 추가된 파일은 이후 commit 명령어를 실행하면 저장소에 변화가 반영됨
    ```bash
    git add <파일명>
    git add . # 모든 파일과 디렉터리 전부 staging area에 추가
    ```
    add된 파일들은 `git status` 실행 시 다음과 같이 표시된다.
    ```bash
    On branch master
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
        modified:   week01/git_command.md
    ```
    week01/git_command.md 파일이 수정되었고 다음 commit시 반영될 것을 알 수 있다.

- ### git commit
  - staged된 파일들의 변화가 기록된다.<br>
  - -m 옵션을 사용해 메시지를 남기거나 
    ```bash
    git commit -m "커밋 메시지"
    ```
    --amend 옵션을 사용해 최근 커밋을 덮어쓸 수 있다.
    ```bash
    git commit -m "수정" --amend
    ```
- ### git log
    - 저장소의 커밋을 정보를 확인할 수 있다.
    - --graph 옵션을 사용하면 커밋 그래프를 확인할 수 있고, --oneline 옵션을 사용하면 기록은 간단한 형태로 확인할 수 있다.
      ```bash
      git log --graph --oneline
      ```
- ### git reset

- ### git fetch
- 
- ### git pull
- 
- ### git reflog
- 
- ### git branch
- 
- ### git checkout
- 
- 


- ### git push
- ### git merge
- ### git rebase
- ###