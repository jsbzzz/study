Tutorial

\#==========================================================================#

\## 기본 설정 ##

\#==========================================================================#

git remote add origin \[원격저장소(Github)주소]            # git remote는 git을 원격저장소에 저장하는 앤드포인트

git clone \[원격저장소(Github)주소]                             # 원격저장소의 파일 가져오기





\#==========================================================================#

\## 소스 기록 ##

\#==========================================================================#

git add .                              # 소스를 업로드

git add . -f                           # ignore 파일이나, 삭제한 파일 이력까지 커밋

git remote show origin          # origin에 리모트 주소가 잘 등록되었는지 확인

git status                             # 파일 추적상태 확인

git commit                           # Staged 상태의 파일을 커밋

git commit -m "커밋 메시지"   # -m, 커밋 메시지 작성

git commit -m "커밋 메시지" --amend              # 이전 커밋 덮어씌우기



\#==========================================================================#

\## 소스 업데이트 ##

\#==========================================================================#

git pull origin main          		 # main 브랜치를 pull하여 업데이트

git fetch origin main      		 # main 브랜치를 fetch하여 업데이트



\#==========================================================================#

\## 소스 복원 ##

\#==========================================================================#

git reset HEAD^ \[강도]                        # 이전 버전으로 리셋     HEAD^ : 현재 커밋(HEAD)의 부모 커밋 == HEAD\~1

git reset HEAD\~2                                    # 2단계 이전으로  

git reset 991ee8c                                     # 특정 리비전 기록으로

\--soft : 기존의 인덱스와 워킹트리를 보존

\--hard : 기존의 인덱스와 워킹트리를 버림

\--mixed : 기존의 인덱스는 버리고 워킹트리를 보존



\#==========================================================================#

\## 브랜치 ##

\#==========================================================================#

git branch \[브랜치명]                   # 새로운 브랜치 생성

git branch -d \[브랜치명]               # 브랜치 삭제

git checkout \[브랜치명]                # 생성된 브랜치 접속

git checkout -b \[브랜치명]            # 새 브랜치 생성 및 접속

git push \[브랜치명]                      # 새 브랜치를 원격저장소(Github)에 저장



\#==========================================================================#

\## 소스 병합 ##

\#==========================================================================#

git rebase                                   # 브랜치의 시작점을 옮겨 커밋을 다시 만듬

git merge                                   # 브랜치의 이력을 그대로 유지한 채 병합

git checkout -f \[현재 브랜치]

git merge \[대상 브랜치]

main => # 변경확인 

sub => # 변경확인 12345

git checkout -f main => # 변경확인

git merge sub => # 변경확인 12345



\#==========================================================================#

\## 충돌과 해결 ##

\#==========================================================================#

~~<<<<<<< HEAD~~

Strawberry

~~=======~~                                           # 하나를 선택

~~Banana~~

~~>>>>>>> sub~~

git add \*                                              # 수정완료 후 재commit으로 충돌 해결

git commit -m "Solved the conflict issue." 











\-------------------------------------------------------------------------------------------

\# https://www.youtube.com/watch?v=tRZGeaHPoaw\&t=390s



Git

SCM(Source Control Management)

파일관리를 유용하게 해준다(시간이 지나고도 돌아가서 변경점을 확인하고 되돌릴 수 있다.)

\-h  # help    ex) git config -h



clear # 화면 초기화



cd # change directory

cd C:/rokey/Git\_Study

cd..                                 # 돌아가기



git config --global user.name "SongHS"

git config --global user.email "9020shs@gmail.com"



git init                             # git 저장소 만들기, 파일탐색기에는 숨겨져있음

git status                         # 스테이터스 확인

git add 파일명                  # 트래킹 시작

git rm --cached 파일명      # 트래킹 해제

git add --all                     # 폴더 내부 모든 파일 트래킹

git add .                            # 폴더 내부 모든 파일 트래킹



폴더 내부에 .gitignore을 만든 뒤 내부에 \*.txt를 적으면 모든 .txt파일을 git이 트래킹 하지 못하게 할 수 있다.



git commit -m ""               # 코드의 변경 사항을 컴퓨터의 내 기록장에 저장

git diff                             # commit 이후 코드의 변경점을 확인

변경된 파일을 다시 add하면 staging단계



git의 환경

\- working files: 파일 수정

\- staging: commit 대기단계

\- commit: 기록



git restore --staged <파일명>            # staging -> working file

commit을 하면 staging환경의 파일만 commit됨

git commit -a -m ""           			  # working file을 바로 commit하려면 

git rm "파일명"              	     	           # 파일 지우기 rm = remove

git restore --staged "파일명"       	    	      # 지운 파일 복구

git mv  "기존 파일 이름" "새 파일 이름"            # mv == move 파일 이름 바꾸기

git commit -m "커밋 메시지" --amend       # 이전 커밋 덮어씌우기



git log                                                          # 변경점, 시간, 작성자 정보

git log --oneline                                     #  정보 한줄요약

git log -p                                                    # 모든 정보 확인

git reset <해시태그>                           # log에서 찾은 해시태그로 해당 버전으로 돌아갈 수 있음

git rebase - i --root                               # 편집기에 접속해 버전 순서, merge 등 다양한걸 할 수 있음



git branch <브랜치명>                        # 브랜치 생성

git branch                                                 # 브랜치 확인 (현재 브랜치는 \*)

git switch <브랜치명>                         # 브랜치로 이동

git merge -m ""  <브랜치명>             # 브랜치 합치기

git branch -d <브랜치명>                   # 브랜치 삭제

git switch -c <브랜치명>           # 새 브랜치 생성 및 접속









