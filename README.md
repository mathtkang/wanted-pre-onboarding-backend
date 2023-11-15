해당 repository는 ' **2023 10 원티드 프리온보딩 백엔드 인턴십, 선발을 위한 과제** '입니다.

### ✅ 목차
- [1️⃣ 지원자 성명](#-지원자-성명-:-강석영-)
- [2️⃣ 애플리케이션 정보](#-애플리케이션-정보)
- [3️⃣ 서비스 개요 및 요구사항 분석](#-서비스-개요-및-요구사항-분석)
- [4️⃣ 구현 과정 및 의사결정 설명](#-구현-과정-및-의사결정-설명)
- [5️⃣ 구현한 API의 동작을 촬영한 데모 영상 링크](#-구현한-API의-동작을-촬영한-데모-영상-링크)
- [6️⃣ Unit Test](#-Unit-Test)
- [7️⃣ 애플리케이션 실행 방법](#-애플리케이션-실행-방법-(엔드포인트-호출-방법-포함))

<br></br>

## 1️⃣ 지원자 성명 : 강석영 🙋‍♀️
안녕하세요. pythonic 코드를 사랑하고 django, flask, fastapi로 서버 개발을 하는 주니어 개발자 강석영입니다.😊


<br></br>

## 2️⃣ 애플리케이션 정보

### 1. 기술스택
- pyenv & poetry (environment)
- python
- Django(DRF)
- MySQL

### 2. ERD

<img width="600" alt="ERD" src="https://user-images.githubusercontent.com/51039577/274833977-ed9436e0-f717-4a83-a3ef-886bdb14d71c.png">
<!-- data set (of csv) & .env -->

### 3. API 명세
<img width="800" alt="API Spec" src="https://user-images.githubusercontent.com/51039577/276403031-d4b612f4-c948-4c77-a354-b5c534d7cd3c.png">

<br></br>

## 3️⃣ 서비스 개요 및 요구사항 분석

### 1. 서비스 개요
- 기업의 채용을 위한 웹 서비스(의 API)
- 회사는 채용공고를 생성하고, 이에 사용자는 해당 회사에 지원합니다.

### 2. 요구사항 분석

#### [1] 채용공고 등록
- 회사는 아래 데이터와 같이 채용공고를 등록합니다.
- Request
    - HTTP method : POST
    - end-point: `v1/jobs/`
    ```json
    {
        "company_id":1,
        "position": "프론트엔드 개발자 [HR솔루션사업팀]",
        "reward": 500000,
        "description": "[HR솔루션팀] HR솔루션팀은 비즈니스, 개발, 디자인 파트 최고의 팀워크를 가진 팀원들이 모여 불편하고 복잡한 HR SaaS를 혁신하기 위해 원티드스페이스를 만들고 있습니다. 파편화되어있는 HR 서비스들을 한곳에서 관리하고 이를 통해 데이터에 기반한 HR이 될 수 있도록 돕고자 합니다. 근태, 전자 결재, 전자 계약, 평가 등을 통합하는 서비스를 구축하고 한국과 일본에서 서비스하고 있으며, 글로벌 HR SaaS가 되려는 목표를 가지고 있습니다. HR솔루션팀과 함께 세계 시장을 공략할 능력 있고 야망 넘치는 동료를 기다립니다.",
        "technologies": "React"
    }
    ```
- Response
    200
    
#### [2] 채용공고 수정
- 회사는 등록한 채용공고를 수정합니다.
- 해당 회사가 등록한 채용공고만 수정 가능합니다. (타 회사 공고 접근 x)
- 수정 가능한 필드는 `position`, `reward`, `description`, `technologies` 입니다. (JobPosting의 `id` 와 `company_id`는 수정할 수 없음)
- Request
    - HTTP method : PUT
    - end-point: `v1/jobs/<int:id>`
        - [예시] `PUT v1/jobs/1`
    ```json
    {
        "position": "백엔드 개발자",
        "technologies": "python"
    }
    ```
- Response
    ```json
    {
        "company_id":1,
        "position": "백엔드 개발자",   -> UPDATE
        "reward": 500000,
        "description": "[HR솔루션팀] HR솔루션팀은 비즈니스, 개발, 디자인 파트 최고의 팀워크를 가진 팀원들이 모여 불편하고 복잡한 HR SaaS를 혁신하기 위해 원티드스페이스를 만들고 있습니다. 파편화되어있는 HR 서비스들을 한곳에서 관리하고 이를 통해 데이터에 기반한 HR이 될 수 있도록 돕고자 합니다. 근태, 전자 결재, 전자 계약, 평가 등을 통합하는 서비스를 구축하고 한국과 일본에서 서비스하고 있으며, 글로벌 HR SaaS가 되려는 목표를 가지고 있습니다. HR솔루션팀과 함께 세계 시장을 공략할 능력 있고 야망 넘치는 동료를 기다립니다.",
        "technologies": "python"    -> UPDATE
    }
    ```

#### [3] 채용공고 삭제
- 회사는 등록한 채용공고를 삭제합니다.
- DB에서 삭제됩니다. (204반환)
- Request
    - HTTP method : DELETE
    - end-point: `v1/jobs/<int:id>`
        - [예시] `DELETE v1/jobs/1`
- Response
    204

#### [4] 채용공고 전체 목록 조회 기능
- 조회 기능은 Authentication과 상관없이 모든 클라이언트가 조회할 수 있습니다.
- 보여지는 필드는 `company_name`, `company_country`, `company_location`, `position`, `reward`, `technologies`입니다.
- Pagination을 적용하여 20개 이상의 필드는 다음 페이지에서 확인할 수 있습니다.
- Request
    - HTTP method : GET
    - end-point: `v1/jobs/?page=1`
        - next page: `GET v1/jobs/?page=2`
- Response
    ```json
    {
        "count": 6,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "companys": [
                    {
                        "name": "원티드랩",
                        "country": "한국",
                        "location": "서울"
                    }
                ],
                "position": "프론트엔드 개발자 [HR솔루션사업팀]",
                "reward": 500000,
                "technologies": "React"
            },
            {
                "id": 2,
                "companys": [
                    {
                        "name": "원티드랩",
                        "country": "한국",
                        "location": "서울"
                    }
                ],
                "position": "데이터 분석가 [데이터팀]",
                "reward": 500000,
                "technologies": "Python"
            },
            {
                "id": 3,
                "companys": [
                    {
                        "name": "원티드랩",
                        "country": "한국",
                        "location": "서울"
                    }
                ],
                "position": "iOS 개발자 [유저개발팀]",
                "reward": 500000,
                "technologies": "Swift"
            },
            {
                "id": 4,
                "companys": [
                    {
                        "name": "원티드랩",
                        "country": "한국",
                        "location": "서울"
                    }
                ],
                "position": "머신 러닝 엔지니어 [AI팀]",
                "reward": 500000,
                "technologies": "Python"
            },
            {
                "id": 5,
                "companys": [
                    {
                        "name": "어터",
                        "country": "한국",
                        "location": "경기"
                    }
                ],
                "position": "백엔드 개발자(Python, Django)",
                "reward": 500000,
                "technologies": "Python"
            },
            {
                "id": 6,
                "companys": [
                    {
                        "name": "어터",
                        "country": "한국",
                        "location": "경기"
                    }
                ],
                "position": "Flutter 앱 개발자",
                "reward": 500000,
                "technologies": "Flutter"
            }
        ]
    }
    ```
#### [5] 채용공고 '키워드 검색' 기능 (✅선택)
- 조회 기능은 Authentication과 상관없이 모든 클라이언트가 조회할 수 있습니다.
- 보여지는 필드는 `company_name`, `company_country`, `company_location`, `position`, `reward`, `technologies`입니다.
- Pagination을 적용하여 20개 이상의 필드는 다음 페이지에서 확인할 수 있습니다.
- 특정 키워드가 포함된 채용공고를 반환합니다.
    - `keyword='검색하고 싶은 키워드'`로 입력해야 필터링이 이루어집니다.
    - [예시] URL: `v1/jobs/search?keyword='원티드'` OR `jobs/search?keyword='python'`
- Request
    - HTTP method : GET
    - end-point: `v1/jobs/search?keyword='원티드'`
- Response
    ```json
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "companys": [
                    {
                        "name": "원티드랩",
                        "country": "한국",
                        "location": "서울"
                    }
                ],
                "position": "데이터 분석가 [데이터팀]",
                "reward": 500000,
                "technologies": "Python"
            },
            {
                "id": 4,
                "companys": [
                    {
                        "name": "원티드랩",
                        "country": "한국",
                        "location": "서울"
                    }
                ],
                "position": "머신 러닝 엔지니어 [AI팀]",
                "reward": 500000,
                "technologies": "Python"
            },
            {
                "id": 5,
                "companys": [
                    {
                        "name": "어터",
                        "country": "한국",
                        "location": "경기"
                    }
                ],
                "position": "백엔드 개발자(Python, Django)",
                "reward": 500000,
                "technologies": "Python"
            }
        ]
    }
    ```

#### [6] 채용공고 상세 정보 조회
- 조회 기능은 Authentication과 상관없이 모든 클라이언트가 조회할 수 있습니다.
- 보여지는 필드는 `company_name`, `company_country`, `company_location`, `position`, `reward`, `technologies`입니다. ('채용내용' 필드가 추가되었음)
- 해당 회사의 다른 채용 공고의 id 목록을 list로 함께 반환합니다. (✅선택)
- Request
    - HTTP method : GET
    - end-point: `/jobs/<int:id>`
        - [예시] `GET /jobs/1`
- Response
    ```json
    {
        "id": 1,     
        "companys": [
            {
                "name": "원티드랩",
                "country": "한국",
                "location": "서울"
            }
        ],
        "position": "프론트엔드 개발자 [HR솔루션사업팀]",
        "description": "[HR솔루션팀] HR솔루션팀은 비즈니스, 개발, 디자인 파트 최고의 팀워크를 가진 팀원들이 모여 불편하고 복잡한 HR SaaS를 혁신하기 위해 원티드스페이스를 만들고 있습니다. 파편화되어있는 HR 서비스들을 한곳에서 관리하고 이를 통해 데이터에 기반한 HR이 될 수 있도록 돕고자 합니다. 근태, 전자 결재, 전자 계약, 평가 등을 통합하는 서비스를 구축하고 한국과 일본에서 서비스하고 있으며, 글로벌 HR SaaS가 되려는 목표를 가지고 있습니다. HR솔루션팀과 함께 세계 시장을 공략할 능력 있고 야망 넘치는 동료를 기다립니다.",
        "technologies": "React",
        "reward": 500000,
        "other_job_postings": [2, 3, 4, 19, 24]   -> 해당 회사의 다른 채용 공고의 id 목록
    }
    ```

#### [7] 사용자의 채용공고 지원 기능 (✅선택)
- 사용자는 채용공고를 보고 지원합니다.
- 사용자는 1회만 지원 가능합니다. (이미 지원한 이력이 있다면 재지원은 불가능합니다.)
- Request
    - HTTP method : POST
    - end-point: `v1/profiles/applied`
- Response
    ```json
    {
        "detail": "채용공고에 성공적으로 지원하였습니다."
    }
    ```
    OR
    ```json
    {
        "detail": "이미 이 채용공고에 지원하였습니다."
    }
    ```
<br></br>

## 4️⃣ 구현 과정 및 의사결정 설명

1. 채용공고 목록 조회, 키워드 필터링 조회 시 Pagination 되도록 구현하였습니다.
    - 데이터를 작은 단위로 나누어 처리하면 서버 부하를 감소시킬 수 있고 이는 성능 개선으로 연결됩니다.
    - DRF에서 제공하는 generics view 사용하여 구현하였습니다.
2. '모든 채용공고 목록 조회', '키워드 목록 조회', '특정 채용공고 내용 반환' 기능들은 로그인 없이 사용 가능하도록 구현했습니다.
    - 그 외 생성, 수정, 삭제 기능은 로그인이 필수이고 DRF의 권한(Permission)을 사용하여, 클라이언트가 User인지 Company인지에 따라 서버에서 다르게 요청 처리하였습니다..
3. 채용공고 지원하는 API를 구현할 때 RESTful API를 지키기위해 고민하였습니다.
    - 처음에는 같은 end-point(`/jobs/<int:jpid>`)에서 GET(모든 유저 접근 가능), PUT & DELETE(회사 권한), POST(유저 권한)으로 생각하고 구현하였습니다.
    - 그러나 권한에 따른 로직을 추가하는 것 보다 end-point를 하나 더 생성하는게 클라이언트 측에서 더 명확하게 이해할 것이라는 생각에, `/jobs/<int:jpid>`은 GET, PUT, DELETE로 구현하고 `/jobs/<int:jpid>/apply`은 POST인 end-point를 하나 더 생성하였습니다.
4. Repository에 구현할 부분들을 세분화 하여 issue로 등록, 해당 이슈 번호를 git message로 함께 적으며 commit 진행하였습니다.
5. 회원가입 API는 만들지 않고, `python manage.py shell`을 이용하여 직접 DB에 raw query로 User와 Company, JobPositng의 데이터를 넣어줬습니다. (Django 내장 ORM 사용)
    ```shell
    >>> from profiles.models import User
    >>> from jobs.models import Company

    [User 생성]
    >>> user = User(username="user1")
    >>> user.save()

    [Company 생성]
    >>> company = Company(name="원티드랩", country="한국", location="서울",)
    >>> company.save()

    [JobPosting 생성]
    >>> job_posting = JobPosting(
        position="프론트엔드 개발자 [HR솔루션사업팀]",
        reward=500000,
        description="[HR솔루션팀] HR솔루션팀은 비즈니스, 개발, 디자인 파트 최고의 팀워크를 가진 팀원들이 모여 불편하고 복잡한 HR SaaS를 혁신하기 위해 원티드스페이스를 만들고 있습니다. 파편화되어있는 HR 서비스들을 한곳에서 관리하고 이를 통해 데이터에 기반한 HR이 될 수 있도록 돕고자 합니다. 근태, 전자 결재, 전자 계약, 평가 등을 통합하는 서비스를 구축하고 한국과 일본에서 서비스하고 있으며, 글로벌 HR SaaS가 되려는 목표를 가지고 있습니다. HR솔루션팀과 함께 세계 시장을 공략할 능력 있고 야망 넘치는 동료를 기다립니다.",
        technologies="React",
    )
    >>> job_posting.save()

    [Company와 JobPosting 관계(1:N)]
    >>> select_company = Company.objects.get(name="원티드랩")
    >>> select_company.job_posting.add(job_posting)

    [Company와 User 관계(1:1), User의 is_company 필드 업데이트]
    >>> user = User.objects.create(username='원티드랩', is_company=True)
    >>> select_company = Company.objects.get(name="원티드랩")
    >>> user.company = select_company
    >>> user.save()
    ```
6. 더 구현하고 싶은/구현한 부분 (실사용 서비스라 생각하고 추가로 구현한 부분들이 있습니다.)
    - User or Company 계정이 본인 계정을 확인하고 수정할 수 있는 API
    - User가 지금까지 지원했던 JobPosting 목록 확인하는 API
    - 구현해보고 싶은 부분: 북마크 on/off, 북마크한 JobPosting 목록 조회 API

<br></br>

## 5️⃣ 구현한 API의 동작을 촬영한 데모 영상 링크

[데모 영상 링크]()

<br></br>

## 6️⃣ Unit Test

<!-- <img width="800" alt="Test-Code" src=""> -->

<br></br>

## 7️⃣ 애플리케이션 실행 방법 (엔드포인트 호출 방법 포함)
(전제) `python >= 3.11` 과 `mysql >= 8.0` 은 설치되어 있습니다.

#### 1. ZIP으로 다운로드 받거나 git clone을 해줍니다.
```
git clone https://github.com/mathtkang/wanted-pre-onboarding-backend.git
```
[참고] 위의 명령어 뒤에 `.`을 추가하면 현재폴더 바로 하위에 manage.py가 존재하게 됩니다.

#### 2. [google drive link](https://drive.google.com/file/d/1mI3f1veny1swdfNRWpmMkwNxpvo5U1nv/view?usp=sharing)를 통해 `.env` 파일을 다운 받습니다. 
- `.env` 파일 안에는 Django의 SECRET_KEY가 있습니다. (이 SECRET_KEY는 보안상의 문제로 git에 올리지 않습니다.)
- `.env` 파일을 `manage.py` 가 있는 위치에 놓습니다.

#### 3. pyenv와 poetry를 이용해서 가상환경을 세팅해줍니다. (참고하면 좋을 [본인 블로그](https://kkangsg.tistory.com/108) 입니다)
1. pip를 이용해서 pyenv와 poetry를 설치해줍니다.
```
pip install pyenv poetry
```
2. 가상환경을 만드는 명령어
```
pyenv virtualenv (python-version) <environment_name>
(EX. pyenv virtualenv 3.11 wanted-pre)
```
3. (선택) 가상환경이 만들어졌는지 확인 명령어
```
pyenv versions
```
4. 가상환경 적용
```
pyenv local <environment_name>
(EX. pyenv local wanted-pre)
```
- 가상환경을 적용하고 싶은 폴더 위치(wanted-pre-onboarding-backend)에서 위의 명령어 입력
- 위의 명령어 입력시, 현 폴더 위치에 해당 가상환경 이름을 가진 `.python-version` 파일 생성됨
- [참고] `.python-version`는 `.gitignore`에 작성된 파일명입니다.
5. 가상환경 활성화 
```
pyenv shell
```
- `.python-version` 파일있는 위치에서 위의 명령어 입력
- 가상환경 적용하면 자동으로 활성화된다.

#### 4. `pyproject.toml` 을 통해 동일한 환경을 만들어줍니다.
```
poety update
or
poetry lock
```
- 위의 명령어 입력시, 현 폴더 위치에 `poetry.lock` 파일 생성됩니다.

#### 5. `manage.py` 가 있는 위치에서 모델 migration을 해줍니다.
```
python manage.py migrate
```
[참고]
- `python manage.py makemigrations` : 아직 데이터베이스에 적용되지 않음, 데이터베이스 스키마 변경사항을 기록하는 용
- `python manage.py migrate` : 위의 명령어에서 생성된 마이그레이션 파일들을 데이터베이스에 적용
(지금은 두번째 명령어만 작성하는게 맞습니다. 변경사항이 없기 때문입니다.)

#### 6. `manage.py` 가 있는 위치에서 서버를 실행합니다.
```
python manage.py runserver
```
- 필요에 따라 위의 명령어 뒤에 포트번호를 붙입니다.

<br></br>

<!-- ### 🚀 AWS EC2 배포
- [서비스 배포 link](http://:8000/)
- 첫 화면은 `Page not found (404)`가 나오는게 맞습니다! end-point를 추가로 입력해야 구현한 기능들을 볼 수 있습니다.
### 시스템 아키텍처
<img width="800" alt="system" src=""> -->
