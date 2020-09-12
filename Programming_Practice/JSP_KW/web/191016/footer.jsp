<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" errorPage="error.jsp"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<TITLE>ch05 :footer.jsp</TITLE></HEAD>
<BODY>
footer.jsp 에서 출력한  메시지 입니다.
<HR>
<%= request.getParameter("email") %>,
<%= request.getParameter("tel") %>

<%
	out.println(request.getParameter("tel"));
%>
</BODY>
</HTML>