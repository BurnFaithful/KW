<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<style type="text/css">
		table tr
		{
			border: 3px solid black;
		}
	</style>

	<title>영민이의 웹페이지</title>
</head>
<body>
	<div align="center">
		<h2>영민이의 웹페이지</h2>
		<hr>
		
		<table>
		<tr>
			<td>
			<%@ include file="book.jsp" %>
			</td>
		</tr>
		<tr>
			<td>
			<%@ include file="youngminImage.jsp" %>
			</td>
		</tr>
		<tr>
			<td>
			<%@ include file="calculator_v2.jsp" %>
			</td>
		</tr>
		<tr>
			<td>
			<%@ include file="burgerking.jsp" %>
			</td>
		</tr>
		</table>
	</div>
</body>
</html>