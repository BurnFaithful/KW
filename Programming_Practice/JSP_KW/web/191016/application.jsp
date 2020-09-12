<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Application Info</title>
</head>
<body>
<div style="text-align: center">
<h2>ch06 :application 테스트</h2>
<hr>
1. 서버정보 : <%= application.getServerInfo() %> <br>
2. 서블릿 API 버전정보 : <%= application.getMajorVersion() +"."+application.getMinorVersion() %> <br>
3. application.jsp 화일의 실제경로 :<%= application.getRealPath("application.jsp") %> <br>

<hr>
setAttribute 로 username 변수에 "홍길동" 설정<p>
<% application.setAttribute("username","홍길동"); 
	  application.log("username=홍길동");
	  application.setAttribute("count", 0);
%>

<a href="application_result.jsp">확인하기</a>

</div>
</body>
</html>