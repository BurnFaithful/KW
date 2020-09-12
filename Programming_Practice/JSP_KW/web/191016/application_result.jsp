<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="java.io.*"%>
<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE> </TITLE></HEAD>
<BODY>
<div style="text-align: center;">
<H2>application 예제</H2>
<HR>
username 에 설정된 값은 : <%= application.getAttribute("username") %> <P>
<%
	Integer count = (Integer)application.getAttribute("count");
	int cnt = count.intValue()+1;
	application.setAttribute("count",cnt);
%>
count : <%= cnt %>
</div>
</BODY>
</HTML>