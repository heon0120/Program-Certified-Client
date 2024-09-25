# Program-Certified-Client
Authentication Server Communication Client for Program Authentication

## 기능
- 사용자로부터 인증 키를 입력받아 서버에 전송
  
- 서버에서 ZIP 파일 다운로드
  
- 다운로드한 ZIP 파일을 자동으로 해제
  
- 사용자 키를 로컬 JSON 파일에 저장

## 라이선스
이 프로젝트는 [GPL 라이선스](https://www.gnu.org/licenses/gpl-3.0.html)를 따릅니다. 

### 라이선스
- 본 프로그램은 GPL 라이선스를 준수하기 위해 소스를 공개합니다.(PyQt5)
  GPL 라이선스는 소스 코드의 수정, 배포, 사용에 대한 자유를 보장합니다. 그러나 수정된 코드나 파생된 작업도 동일한 라이선스 하에 공개해야 합니다.
  
- 본 애플리케이션은 서버와 통신하는 기능을 포함하고 있습니다. 이 부분은 다른 라이선스를 사용하므로, 해당 코드 및 관련 정보는 공개하지 않습니다.
서버와의 통신에 대한 정보는 별도의 라이선스 조건에 따릅니다. 예) MIT, Apache, PSFL등 소스공개가 의무가 아닌 라이선스.

- 서버는 모두 공개의무가 없는 라이브러리를 사용하기 때문에 공개하지 않습니다.

- 본 애플리케이션의 라이선스관련 문제는 Issues를 사용하여 알려주시면 수정하겠습니다.

## 생략된 코드의 작동

본 애플리케이션은 사용자 인증 및 ZIP 파일 다운로드를 위한 서버와의 통신 기능을 포함하고 있습니다. 이 통신 과정은 다음과 같은 과정을 거칩니다:

1. **인증 키 입력**: 사용자는 애플리케이션의 UI에서 인증 키를 입력합니다. 이 키는 서버에서 유효성을 검사하는 데 사용됩니다.

2. **공개 IP 주소 획득**: 애플리케이션은 사용자의 공개 IP 주소를 자동으로 가져옵니다. 이는 서버와의 통신에서 사용자 식별 및 인증을 위한 중요한 정보입니다.

3. **서버 요청**: 사용자가 입력한 인증 키와 공개 IP 주소는 JSON 형식으로 서버에 POST 요청을 통해 전송됩니다. 이 요청은 HTTP 프로토콜을 사용하여 수행되며, 애플리케이션의 정상적인 작동을 위해 필수적입니다.

4. **서버 응답 처리**: 서버는 요청을 처리한 후, 응답으로 ZIP 파일을 포함한 데이터 또는 오류 메시지를 반환합니다. 성공적인 요청의 경우, 서버는 ZIP 파일을 다운로드할 수 있는 링크를 포함합니다.

5. **ZIP 파일 다운로드**: 애플리케이션은 서버 응답에서 제공된 ZIP 파일을 다운로드합니다. 이 ZIP 파일은 사용자가 요청한 리소스를 포함하고 있으며, 다운로드가 완료되면 자동으로 압축 해제됩니다.

6. **데이터 보안**: 서버와의 모든 통신 과정은 보안을 고려하여 설계되었습니다. HTTPS 프로토콜을 통해 데이터가 암호화되어 전송되며, 민감한 정보는 서버에서 안전하게 저장 및 처리됩니다.

통신 라이브러리는 Requests를 사용하며 압축은 zipfile라이브러리를 사용합니다.
