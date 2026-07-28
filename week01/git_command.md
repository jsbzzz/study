## git의 작동 방식
- ### git의 구조
  - Working Directory : 현재 작업 중인 공간
  - Staging Area : 커밋될 변경 사항을 임시로 저장하는 공간
  - Repository : 모든 파일과 폴더의 기록을 저장하는 공간
  - HEAD: 본인의 현재 위치를 가리키는 포인터.  
    HEAD의 위치를 옮기면 내 Working Directory와 Staging Area도 HEAD의 상태와 동기화 된다.
  - Tip, head(s) : 브랜치의 가장 끝부분

- ### git에서 관리하는 파일 상태
  - Untracked : git에서 추적하고 있지 않은 상태. 새로 생성되거나 가져온 파일
  - Tracked : git에서 추적하는 상태.
    - Staged : `git add <파일>` 명령어 실행 시 파일은 staged 상태가 된다.<br>
      이후 commit 실행 시 해당 파일의 변경사항이 repository에 저장된다.
    - Unmodified : 마지막 커밋된 이후 변경사항이 없는 상태
    - Modified : working directory의 파일이 마지막에 staging된 때와 다른 상태
  
  - 파일의 상태는 `git status` 명령어로 확인 가능.<br>
    하지만 일반적으로는 커밋될 지 여부만 확인하면 충분.
   
   
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
  - 저장소의 상태를 확인하는 명령어.
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
- ### git branch
  - 서로 영향을 주지 않는 독릭적인 작업 공간을 만들 수 있다.
     ```bash
      git branch # 브랜치 목록 확인 -r 옵션으로 원격 브랜치 확인, -a 옵션으로 모든 브랜치 확인
      git branch <브랜치> # 브랜치 생성
      git branch -m <새로운 브랜치> # 현재 브랜치의 이름을 새로운 브랜치 이름으로 변경
      git branch -m <이전 브랜치> <새로운 브랜치> # 이전 브랜를 새로운 브랜치 이름으로 변경
      git branch -d <브랜치> # 브랜치 삭제 -D 옵션은 강제 삭제
      ```

- ### git checkout
  - 브랜치를 이동할 때 `git checkout <브랜치>` 명령어 사용
  - 과거의 파일이나 폴더를 가져와 덮어 쓰는 경우
  
    - `git checkout <파일명>` 파일을 **staging area**의 내용으로 덮어 쓴다.<br>
      아예 최근 커밋의 상태로 되돌리려면 `git restore --staged <파일명>` 후 `git restore <파일명>`을 사용하거나 아래의 명령어를 활용해야 한다.
    
    - `git checkout <커밋> <파일명>` Working Directory, Staging Area를 해당 커밋에서의 내용으로 덮어쓴다.
  - 특정 커밋의 상태로 덮어쓰려면 `git checkout <커밋>` 사용. 이 경우 Working Directory,      Staging Area, Repository가 모두 해당 커밋 상태로 비뀌게 됨.<br>
    - 다시 최근 커밋으로 돌아가려면 `git checkout <브랜치>`를 사용.<br>
    - 만약 해당 상태에서 수정한 경우
      - 커밋하지 않고 `git checkout <브랜치>`로 되돌아오면 **수정 내역**을 함께 가져오게 됨.
      - 커밋을 하고 바로 돌아오면 해당 커밋은 소실
      - 커밋을 하고 브랜치까지 만들어야 해당 커밋이 저장 됨.

- ### git restore
  - 파일이나 폴더를 특정 상태로 되돌린다.
    - `git restore <파일명>` 사용 시 Working Directory의 파일을 **Staging Area**의 상태로 복구된다.
    - `git restore --staged <파일명>` --staged 옵션 사용 시 **Staging Area**의 파일을 **HEAD**의 파일로 복구한다.
    - `git restore --source=<커밋> <파일>` 형태로 사용 시 해당 커밋에서의 파일을 Working Directory에만 덮어 쓴다.

- ### git reset
  - 과거 커밋 시점으로 돌아가고 이후의 커밋 기록은 삭제된다.
    - `git reset --soft <커밋>` --soft 옵션 사용 시 Staging Area와 Workin Directory의 내용은 유지된다.
    - `git reset --mixed <커밋>` --mixed 옵션 사용 시 Working Directory의 내용은 유지되지만 Staging Area는 해당 커밋의 내용으로 변경 된다.
    - `git reset --hard <커밋>` --hard 옵션 사용 시 Staging Area, Working Directory의 내용도 해당 커밋의 내용으로 변경 된다.

- ### git merge
  - `git merge <대상 브랜치>` 대상 브랜치의 변경 내역을 현재 브랜치로 가져와 병합한다. merge에는 다음과 같은 두가지 형태가 있다.
    - Fast-Forward : 현재 브랜치에 추가된 커밋이 없을 때 브랜치의 포인터만 대상 브랜치의 최신 커밋으로 옮긴다.
    - 3-Way Merge : 두 브랜치의 작업 내용을 합치는 새로운 Merge Commit을 하나 만들고 현재 브랜치의 포인터를 해당 커밋으로 옮긴다.  
      만약 두 브랜치에서 파일의 한 부분을 동시에 수정했다면 충돌(Conflict)가 발생한다.  
      이 경우 충돌이 일어난 부분을 직접 수정하고 다시 commit해야 병합이 완료된다.

- ### git rebase
  - 현재 브랜치가 파생된 기준점을 대상 브랜치의 최신 커밋으로 재설정한다.  
    - `git rebase <대상브랜치>` 명령어 실행 시 **현재 브랜치**의 커밋들이 대상 브랜치의 최신 커밋 위에 이어붙여진다.  
    - 이때 이동한 것은 현재 브랜치뿐이므로, 대상 브랜치의 [팁](#git의-구조)(Tip)은 여전히 과거의 제자리에 머물러 있다.
  - 충돌(Conflict) 발생 시 
    - 파일 수정 후 `git add` 및 `git rebase --continue`를 입력한다.
    - 수정 내역을 적용하지 않으려면 `git rebase --skip`을 입력한다.
    - rebase 자체를 취소하려면 `git rebase --abort`를 입력한다.
  - rebase 이후
      - 대상 브랜치로 이동 후 merge할 경우 Fast-Forward merge되어 분기된 흔적이 남지 않는다.
      - 대상 브랜치로 이동 후 merge하지 않고 새로운 커밋을 생성할 경우 해당 위치부터 브랜치가 분기된다.

- ### git fetch
 
- ### git diff

- ### git pull

- ### git reflog

- ### git push
- ###