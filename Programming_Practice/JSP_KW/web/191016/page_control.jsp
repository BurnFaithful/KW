<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<HTML>
<HEAD><TITLE>ch06 : page_control.jsp</TITLE></HEAD>
<BODY>
<H2>forward, sendRedirect 테스트</H2>
<HR>
<form method=post action=forward_action2.jsp>
	forward action : <input type=text name=username>
	<input type=submit value="확인">
</form>

<form method=post action=response_sendRedirect.jsp>
	response.sendRedirect : <input type=text name=username>
	<input type=submit value="확인">
</form>
</BODY>
</HTML>