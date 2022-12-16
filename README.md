# API_ssokssok
Flask API Server for ColorSsokSsok Aplication


Color SsokSsok API 엔드포인트
서버 호스팅 주소 :  https://apissokssok-m52f5s4c4q-du.a.run.app



FBAuth

로그인 API
엔드포인트 URL : /auth/signin
요청 방식 : POST
데이터 전달 : form-data: {email : "", password:""}
결과값 : 성공 시 - {token : ""},200 실패 시 - {message:"There was an error while logging in"},400

회원가입 API
엔드포인트 URL : /auth/signup
요청 방식 : POST
데이터 전달 : form-data: {email : "", password:"", displayName : ""}
결과값 : 성공 시 - {message : "Successfully create user {$USER_Valid_Key}},200 실패 시 - 1. 이메일이 NULL 일 때 {"Username i s Missing"},400 2. Password가 비어 있을 때 {"Password is Missing"},400 3. 계정 생성에 실패했을 때(계정 중복, 이메일 형식 혹은 비밀번호 부적합) : "Error occur in creating user"



ImageProcess

이미지 처리 API
엔드포인트 URL : /image/processing
요청 방식 : POST
데이터 전달 : form-data: {filename : ""}
결과값 : 성공 시 - {{$Converted_Image_URL}},200

내 이미지 불러오기(전체)
엔드포인트 URL : /image/myfiles
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token
결과값 : 성공 시 - [[{$filename},{$Image_URL}],...],200

내 이미지 불러오기(원본)
엔드포인트 URL : /image/myfiles/beforeConvert
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token
결과값 : 성공 시 - [[{$filename},{$Image_URL}],...],200

내 이미지 불러오기(도안)
엔드포인트 URL : /image/myfiles/afterConvert
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token
결과값 : 성공 시 - [[{$filename},{$Image_URL}],...],200

내 이미지 불러오기(색칠 중)
엔드포인트 URL : /image/myfiles/Coloring
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token
결과값 : 성공 시 - [[{$filename},{$SVG_URL}],...],200

내 이미지 불러오기(색칠 완료)
엔드포인트 URL : /image/myfiles/Submit
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token
결과값 : 성공 시 - [[{$filename},{$Image_URL}],...],200

내 이미지 불러오기(파일 별 그룹화)
엔드포인트 URL : /image/myfiles/groupby
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token
결과값 : 성공 시 - [[Image : {$Image_URL}, ConvertedImage: {$Image_URL}, SVG : {$SVG_URL}],...],200

특정 파일 불러오기(원본)
엔드포인트 URL : /image/getfile/beforeConvert?filename=""
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
결과값 : 성공 시 - {$Image_URL},200

특정 파일 불러오기(도안)
엔드포인트 URL : /image/getfile/afterConvert?filename=""
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
결과값 : 성공 시 - {$Image_URL},200

특정 파일 불러오기(색칠중)
엔드포인트 URL : /image/getfile/Coloring?filename=""
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
결과값 : 성공 시 - {$SVG_URL},200

특정 파일 불러오기(완성본)
엔드포인트 URL : /image/getfile/Submit?filename=""
요청 방식 : GET
데이터 전달 : Header - Authorization : jwt token / URI - filename : ""
결과값 : 성공 시 - {$Image_URL},200

