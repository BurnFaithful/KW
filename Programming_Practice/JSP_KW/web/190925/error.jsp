<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" isErrorPage="true" %>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<div align="center">
		<h2>처리 중 문제가 발생하였습니다.</h2>
		<hr>
		<table>
		<tr bgcolor="orange">
			<td>
				관리자에게 문의해 주세요! <br>
				빠른 시일 내에 복구하겠습니다.
				<hr>
				<%= exception %>
			</td>
		</table>
	</div>
</body>
</html>