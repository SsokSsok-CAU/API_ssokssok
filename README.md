# API_ssokssok

Flask API Server for ColorSsokSsok Aplication

### Color SsokSsok API 엔드포인트

```
`https://apissokssok-m52f5s4c4q-du.a.run.app`
```

# FBAuth

## 로그인 API

### Request

`POST /auth/signin`

### Request BODY

```
form-data: {email : "", password:""}
```

### Response - success

```
{token : ""},200
```

### Response - fail

```
{message:"There was an error while logging in"},400
```

## 회원가입 API

### Request

`POST /auth/signup`

### Request BODY

```
form-data: {email : "", password:"", displayName : ""}
```

### Response - success

```
{'token':{$JWT Token},'displayName':{$displayName}}200
```

### Response - fail

```
1. 이메일이 NULL 일 때 {"Username i s Missing"},400
2. Password가 비어 있을 때 {"Password is Missing"},400
3. 계정 생성에 실패했을 때(계정 중복, 이메일 형식 혹은 비밀번호 부적합) : "Error occur in creating user"
```

## 비밀번호 분실 API

### Request

`POST /auth/forgotPassword

### Request BODY

```
form-data: {email : ""}
```

### Response - success

```
200
```

### Response - fail

```
{message:"There was an error while logging in"},400
```

# ImageProcess

## 이미지 처리 API

### Request

`POST /image/processing`

### Request BODY

```
form-data: {filename : ""}
```

### Response - success

```
{{$Converted_Image_URL}},200
```

## 내 이미지 불러오기(전체)

### Request

`GET /image/myfiles`

### Request Header

```
Authorization : jwt token
```

### Response - success

```
[[{$filename},{$Image_URL}],...],200
```

## 내 이미지 불러오기(원본)

### Request

`GET /image/myfiles/beforeConvert`

### Request Header

```
Authorization : jwt token
```

### Response - success

```
[[{$filename},{$Image_URL}],...],200
```

## 내 이미지 불러오기(도안)

### Request

`GET /image/myfiles/afterConvert`

### Request Header

```
Authorization : jwt token
```

### Response - success

```
[[{$filename},{$Image_URL}],...],200
```

## 내 이미지 불러오기(색칠 중)

### Request

`GET /image/myfiles/Coloring`

### Request Header

```
Authorization : jwt token
```

### Response - success

```
[[{$filename},{$SVG_URL}],...],200
```

## 내 이미지 불러오기(색칠 완료)

### Request

`GET /image/myfiles/Submit`

### Request Header

```
Authorization : jwt token
```

### Response - success

```
[[{$filename},{$Image_URL}],...],200
```

## 내 이미지 불러오기(파일 별 그룹화)

### Request

`GET /image/myfiles/groupby`

### Request Header

```
Authorization : jwt token
```

### Response - success

```
[[Image : {$Image_URL}, ConvertedImage: {$Image_URL}, SVG : {$SVG_URL}],...],200
```

## 특정 파일 불러오기(원본)

### Request

`GET /image/getfile/beforeConvert?filename=""`

### Request Header

```
데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
```

### Response - success

```
결과값 : 성공 시 - {$Image_URL},200
```

## 특정 파일 불러오기(도안)

### Request

`GET /image/getfile/afterConvert?filename=""`

데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
결과값 : 성공 시 - {$Image_URL},200

## 특정 파일 불러오기(색칠중)

### Request

`GET /image/getfile/Coloring?filename=""`

### Request Header

```
Authorization : jwt token / URI - filename : ""
```

### Response - success

```
결과값 : 성공 시 - {$SVG_URL},200
```

## 특정 파일 불러오기(완성본)

### Request

```
`GET /image/getfile/Submit?filename=""`
```

### Request Header

```
데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
```

### Response - success

```
결과값 : 성공 시 - {$Image_URL},200
```
