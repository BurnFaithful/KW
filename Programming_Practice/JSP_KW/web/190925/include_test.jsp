<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="banner.css">
	<title>include 지시어 테스트</title>
</head>
<body>
	<div align="center">
		<h2> include 지시어 테스트</h2>
		<hr>
		
		<%@ include file="menu.jsp" %>
		<p>
		<table>
			<tr>
				<td><%@ include file="news.jsp" %></td>
				<td width="30">&nbsp;</td>
				<td><%@ include file="shopping.jsp" %></td>
				<td><%@ include file="image.jsp" %></td>
			</tr>
		</table>
	</div>
</body>
</html>