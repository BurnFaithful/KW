<%@ page import="java.util.*, java.text.*" %>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ch03 : Hello, World</title>
</head>
<body>
	<div align="center">
		<h2>Hello World : 헬로 월드</h2>
		<hr>
		<% 
		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.KOREA);
		Date curTime = new Date(); 
		%>
		현재 날짜와 시간은 : <%= formatter.format(curTime) %>
	</div>
</body>
</html>