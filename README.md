해당 repository는 ' **2023 10 원티드 프리온보딩 백엔드 인턴십, 선발을 위한 과제** '입니다.

### ✅ 목차
- 1️⃣ [지원자 성명]()
- 2️⃣ [애플리케이션 정보]()
- 3️⃣ [서비스 개요 및 요구사항 분석]()
- 4️⃣ [구현 과정 및 의사결정 설명]()
- 5️⃣ [구현한 API의 동작을 촬영한 데모 영상 링크]()
- 6️⃣ [API 명세(request/response 포함)]()
- 7️⃣ [Unit Test]()
- 8️⃣ [애플리케이션 실행 방법 (엔드포인트 호출 방법 포함)]()

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

<img width="500" alt="ERD" src="https://user-images.githubusercontent.com/51039577/274833977-ed9436e0-f717-4a83-a3ef-886bdb14d71c.png">
<!-- data set (of csv) & .env -->


<br></br>

## 3️⃣ 서비스 개요 및 요구사항 분석

### 1. 서비스 개요
- 기업의 채용을 위한 웹 서비스(의 API)
- 회사는 채용공고를 생성하고, 이에 사용자는 해당 회사에 지원합니다.

### 2. 요구사항 분석

#### [1] 채용공고 등록
- 회사는 아래 데이터와 같이 채용공고를 등록합니다.
    ```json
    {
        "company_id":1,
        "position": "프론트엔드 개발자 [HR솔루션사업팀]",
        "reward": 500000,
        "description": "[HR솔루션팀] HR솔루션팀은 비즈니스, 개발, 디자인 파트 최고의 팀워크를 가진 팀원들이 모여 불편하고 복잡한 HR SaaS를 혁신하기 위해 원티드스페이스를 만들고 있습니다. 파편화되어있는 HR 서비스들을 한곳에서 관리하고 이를 통해 데이터에 기반한 HR이 될 수 있도록 돕고자 합니다. 근태, 전자 결재, 전자 계약, 평가 등을 통합하는 서비스를 구축하고 한국과 일본에서 서비스하고 있으며, 글로벌 HR SaaS가 되려는 목표를 가지고 있습니다. HR솔루션팀과 함께 세계 시장을 공략할 능력 있고 야망 넘치는 동료를 기다립니다.",
        "technologies": "React"
    }
    ```
#### [2] 채용공고 수정
- 회사는 등록한 채용공고를 수정합니다.
- 해당 회사가 등록한 채용공고만 수정 가능합니다. (타 회사 공고 접근 x)
- 수정 가능한 필드는 `position`, `reward`, `description`, `technologies` 입니다. (`채용공고_id` 와 `회사_id`는 수정할 수 없음)

#### [3] 채용공고 삭제
- 회사는 등록한 채용공고를 삭제합니다.
- DB에서 삭제됩니다. (204반환)

#### [4] 채용공고 전체 목록 조회 기능
- 조회 기능은 Authentication과 상관없이 모든 클라이언트가 조회할 수 있습니다.
- 보여지는 필드는 `company_name`, `company_country`, `company_location`, `position`, `reward`, `technologies`입니다.
- Pagination을 적용하여 20개 이상의 필드는 다음 페이지에서 확인할 수 있습니다.
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
- [예시] URL: `v1/jobs/1`
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
        "other_job_postings": [2, 3, 4, 19, 24]
    }
    ```

#### [7] 사용자의 채용공고 지원 기능 (✅선택)
- 사용자는 채용공고를 보고 지원합니다.
- 사용자는 1회만 지원 가능합니다. (이미 지원한 이력이 있다면 재지원은 불가능합니다.)
    ```json
    {
        "채용공고_id": 채용공고_id,
        "사용자_id": 사용자_id
    }
    ```

<br></br>

## 4️⃣ 구현 과정 및 의사결정 설명

<!-- 1. Django(DRF)와 MySQL을 사용해서 router를 구현하였고, AWS EC2를 사용해서 배포를 진행했습니다.
2. ORM은 django에 내장되어 있는 ORM을 사용했습니다.
3. RESTful API로 설계하고 구현했습니다. HTTP 프로토콜을 기반으로 하고 있어 간단하고 직관적이며 테스트하기에 용이한 디자인입니다.
4. email과 password의 유효성 검사를 위해 Django의 EmailValidator를 사용하여 User모델의 email필드에 유효성 검사를 진행하였고, ModelSerializer를 상속받아서 password validation을 위한 serializer를 구현했습니다.
8. password를 암호화할 때 bcrypt를 사용할지 Django의 User모델에서 제공하는 set_password()를 사용할지 고민했습니다. 공식문서를 찾아보니 set_password()도 기본적으로 bcrypt 알고리즘을 사용한다고 하고, (Monolithic한) Django를 사용한다면 제공하는 메서드를 사용하는 것이 개발자의 입장에서 더 편리할 것이라는 생각에 set_password()를 사용하여 password를 암호화 했습니다.
9. JWT 인증 방식은 서버에 세션 정보를 저장하지 않고 클라이언트에서 토큰을 관리하는 방식(stateless)으로 서버의 부담이 적고 확장이 용이합니다.
10. Pagination을 통해 데이터를 작은 단위로 나누어 처리하면 서버 부하를 감소시킬 수 있고 이는 성능 개선으로 연결됩니다. 저는 DRF(Django Rest Framework)에서 제공하는 ListAPIView를 상속받아서 구현하였습니다.
11. '게시글 목록 조회 기능'과 '특정 게시글 조회 기능'은 로그인 하지 않아도 사용할 수 있도록 구현했습니다. 그 외 생성, 수정, 삭제 기능은 로그인이 필수입니다. -->

<!-- - 레포지토리에 이슈 등록하고, 해당 이슈 번호를 git message에 적으면서 커밋 진행 -->


- 더 구현하고 싶은 부분

<br></br>

## 5️⃣ 구현한 API의 동작을 촬영한 데모 영상 링크

[데모 영상 링크]()

<br></br>

## 6️⃣ API 명세(request/response 포함)
<img width="800" alt="API Spec" src="https://user-images.githubusercontent.com/51039577/275731962-fe0a2bfd-2a5c-4292-b2d1-e72e5f6fe5e3.png">

<!-- ### 1. Auth
**1. 회원가입**
- End-point: `/auth/signup`
- Request
    - Method: `POST`
    - Permissions: `AllowAny`
    - Request Body
    ```json
    {
        "email": "wanted@gmail.com",
        "password": "preonboarding1234"
    }
    ```
- Response
    1. Successful Response
        - 회원가입시 입력했던 email 반환
        ```
        HTTP 201 Created
        {
            "email": "wanted@gmail.com",
        }
        ```
    2. Error Response
        - email or password를 입력하지 않은 경우
        ```
        HTTP 400 Bad Request
        {
            "detail": "잘못된 요청입니다. email, password 모두 존재해야 합니다."
        }
        ```
    3. Error Response
        - 이미 있는 email로 입력한 경우
        ```
        HTTP 409 Conflict
        {
            "email": [
                "사용자의 email은/는 이미 존재합니다."
            ]
        }
        ```
    4. Error Response
        - (유효성 검사) email에 @와 .이 없는 경우 or password가 8자 미만인 경우
        ```
        HTTP 409 Conflict
        {
            "email": [
                "이메일 주소가 올바르지 않습니다. @와 .을 포함해주세요.",
                "유효한 이메일 주소를 입력하십시오."
            ],
            "password": [
                "비밀번호는 최소 8자 이상이어야 합니다."
            ]
        }
        ```

**2. 로그인**
- End-point: `/auth/jwt-login`
- Request
    - Method: `POST`
    - Permissions: `AllowAny`
    - Request Body
    ```json
    {
        "email": "wanted@gmail.com",
        "password": "preonboarding1234"
    }
    ```
- Response
    1. Successful Response
        - JWT(JSON Web Token) 생성 후 발급
        ```
        HTTP 200 OK
        {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCIkpXVCJ9.eyJpI6NX0.6lNgRKpo1ALnwtvUO0ifdhTWUCO2Q1ylVVVLt1c"
        }
        ```
    2. Error Response
        - email or password를 입력하지 않은 경우
        ```
        HTTP 400 Bad Request
        {
            "detail": "잘못된 요청입니다. email, password 모두 존재해야 합니다."
        }
        ```
    3. Error Response
        - (유효성 검사) email은 맞게 입력했으나 password가 8자 미만인 경우
        ```
        HTTP 400 Bad Request
        {
            "detail": "비밀번호는 8자 이상으로 입력해야 합니다."
        }
        ```
    4. Error Response
        - email은 맞게 입력했으나 password가 틀린 경우
        ```
        HTTP 400 Bad Request
        {
            "detail": "The password is wrong."
        }
        ```

### 2. Post

**1. 게시글 목록 조회 (pagination 적용)**
- End-point: `/posts/?page=1`
- Request
    - Method: `GET`
    - Permissions: `AllowAny`
- Response
    1. Successful Response
        - page num = 10
        ```
        HTTP 200 OK
        {
            "count": 13,
            "next": "http://127.0.0.1:8080/posts/?page=2",
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "title": "test-update",
                    "content": "test-content-update",
                    "created_at": "2023-08-06T03:14:31.724124",
                    "updated_at": "2023-08-06T03:15:28.439069",
                    "create_user": 1
                },
                {
                    "id": 2,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:14:41.829987",
                    "updated_at": "2023-08-06T03:14:41.830002",
                    "create_user": 1
                },
                {
                    "id": 3,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:14:43.912871",
                    "updated_at": "2023-08-06T03:14:43.912889",
                    "create_user": 1
                },
                {
                    "id": 4,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:14:46.613152",
                    "updated_at": "2023-08-06T03:14:46.613167",
                    "create_user": 1
                },
                {
                    "id": 5,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:29:33.125022",
                    "updated_at": "2023-08-06T03:29:33.125045",
                    "create_user": 3
                },
                {
                    "id": 6,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:29:36.398625",
                    "updated_at": "2023-08-06T03:29:36.398672",
                    "create_user": 3
                },
                {
                    "id": 7,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:29:59.518612",
                    "updated_at": "2023-08-06T03:29:59.518630",
                    "create_user": 3
                },
                {
                    "id": 8,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:30:05.243543",
                    "updated_at": "2023-08-06T03:30:05.243567",
                    "create_user": 3
                },
                {
                    "id": 9,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:30:07.483671",
                    "updated_at": "2023-08-06T03:30:07.483690",
                    "create_user": 3
                },
                {
                    "id": 10,
                    "title": "test",
                    "content": "test-content",
                    "created_at": "2023-08-06T03:30:09.943902",
                    "updated_at": "2023-08-06T03:30:09.943920",
                    "create_user": 3
                }
            ]
        }
        ```

**2. 게시글 생성**
- End-point: `/posts`
- Request
    - Method: `POST`
    - Permissions: `IsAuthenticated`
    - Headers: 'Authorization: Bearer {JWT}'
    - Request Body
    ```json
    {
        "title": "create title",
        "content": "create content"
    }
    ```
- Response
    1. Successful Response
        - 게시글 생성 완료
        ```
        HTTP 200 OK
        {
            "id": 11,
            "title": "test",
            "content": "test-content",
            "created_at": "2023-08-06T03:30:09.943902",
            "updated_at": "2023-08-06T03:30:09.943920",
            "create_user": 3
        }
        ```
    2. Error Response
        - title or content를 입력하지 않은 경우
        ```
        HTTP 400 Bad Request
        {
            "title": [
                "이 필드는 blank일 수 없습니다."
            ],
            "content": [
                "이 필드는 blank일 수 없습니다."
            ]
        }
        ```

**3. 게시글 조회**
- End-point: `/posts/<int:id>`
    EX) `/posts/1`
- Request
    - Method: `GET`
    - Permissions: `AllowAny`
- Response
    1. Successful Response
        ```
        HTTP 200 OK
        {
            "id": 1,
            "create_user": {
                "email": "sy@gmail.com"
            },
            "title": "test-update",
            "content": "test-content-update",
            "created_at": "2023-08-06T03:14:31.724124",
            "updated_at": "2023-08-06T03:14:31.724124"
        }
        ```
    2. Error Response
        - 찾는 게시글이 존재하지 않는 경우
        ```
        HTTP 404 Not Found
        {
            "detail": "찾을 수 없습니다."
        }
        ```

**4. 게시글 수정**
- End-point: `/posts/<int:id>`
- Request
    - Method: `PUT`
    - Permissions: `IsAuthenticated`
    - Headers: 'Authorization: Bearer {JWT}'
    - Request Body
    ```json
    {
        "title": "update title",
        "content": "update content"
    }
    ```
- Response
    1. Successful Response
        - 게시글 수정 완료
        ```
        HTTP 200 OK
        {
            "id": 1,
            "create_user": {
                "email": "sy@gmail.com"
            },
            "title": "update title",
            "content": "update content",
            "created_at": "2023-08-06T03:14:31.724124",
            "updated_at": "2023-08-06T03:15:28.439069"
        }
        ```
    2. Error Response
        - 내가 작성한 게시글이 아닌 경우 (권한 없음)
        ```
        HTTP 403 Forbidden
        {
            "detail": "해당 post를 수정할 권한이 없음"
        }
        ```

**5. 게시글 삭제**
- End-point: `/posts/<int:id>`
- Request
    - Method: `DELETE`
    - Permissions: `IsAuthenticated`
    - Headers: 'Authorization: Bearer {JWT}'
- Response
    1. Successful Response
        - 게시글 삭제 완료
        ```
        HTTP 204 No Content
        ```
        (당연한 말이지만) 삭제한 이후에는 `HTTP 404 Not Found`로 나온다.
    2. Error Response
        - 내가 작성한 게시글이 아닌 경우 (권한 없음)
        ```
        HTTP 403 Forbidden
        {
            "detail": "해당 post를 삭제할 권한이 없음"
        }
        ``` -->


<br></br>

## 7️⃣ Unit Test

<img width="800" alt="Test-Code" src="">
<!-- (모든 router의 Test code를 구현하진 못했지만 6개 router의 test code를 작성했습니다.) -->


<br></br>

## 8️⃣ 애플리케이션 실행 방법 (엔드포인트 호출 방법 포함)
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

#### 7. End-point 호출 방법 
[참고] Django REST Framework는 admin 패널을 제공합니다. Postman을 사용하지 않아도 (header인증 제외) 웹 상으로 request/response가 가능합니다.

### 1. Auth
1. 회원가입 기능
    - HTTP method : POST
    - end-point: `/auth/signup`
    - json 형식으로 전송
    ```json
    {
        "email": "wanted@gmail.com",
        "password": "preonboarding1234"
    }
    ```
2. 로그인 기능
    - HTTP method : POST
    - end-point: `/auth/jwt-login`
    - json 형식으로 전송
    ```json
    {
        "email": "wanted@gmail.com",
        "password": "preonboarding1234"
    }
    ```
### 2. Post
1. 게시글 목록 조회 (pagination 적용)
    - HTTP method : GET
    - end-point: `/posts/?page=1`
        - next page: `GET /posts/?page=2`
2. 게시글 생성
    - HTTP method : POST
    - end-point: `/posts`
    ```
    - H 'Authorization: Bearer {JWT}'
    - d '{
            "title": "create title",
            "content": "create content"
        }'
    ```
3. 특정 게시글 조회
    - HTTP method : GET
    - end-point: `/posts/<int:id>`
        - EX) `GET /posts/1`
4. 특정 게시글 수정
    - HTTP method : PUT
    - end-point: `/posts/<int:id>`
    ```
    - H 'Authorization: Bearer {JWT}'
    - d '{
            "title": "update title",
            "content": "update content"
        }'
    ```
5. 특정 게시글 삭제
    - HTTP method : DELETE
    - end-point: `/posts/<int:id>`
    ```
    - H 'Authorization: Bearer {JWT}'
    ```

<br></br>

<!-- ### 2. 🚀 AWS EC2 배포
- [서비스 배포 link](http://43.201.153.227:8000/)
- 첫 화면은 `Page not found (404)`가 나오는게 맞습니다! end-point를 추가로 입력해야 구현한 기능들을 볼 수 있습니다.
- 시스템 아키텍처
<img width="800" alt="system" src="https://user-images.githubusercontent.com/51039577/258669658-299e1312-5010-483b-aa59-788909c8701d.png"> -->
