<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head><TITLE>ch06 : page_control_end.jsp</TITLE></HEAD>
<BODY>
<div align="center">
<H2>forward action 및 sendRedirect() 결과</H2>
<HR>
 지금 보이는 화면은 page_control_end.jsp 에서 출력한 결과 입니다.
<HR>
이름 : <%= request.getParameter("username") %> <BR>
전화번호 : <%= request.getParameter("tel") %>
</div>
</BODY>
</HTML>