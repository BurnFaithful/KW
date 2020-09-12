<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.util.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%
	// 한글 캐릭터셋 변환
	request.setCharacterEncoding("UTF-8");
	// HTML 폼에서 username으로 전달된 값을 가지고 옴 
	String username = request.getParameter("username");
	
	// username이 null 이 아닌 경우 세션에 값을 저장
	if(username != null) {
		session.setAttribute("user",username);
	}
%>
<html>
<head>
<title>ch06 : twitter_list.jsp</title>
</head>
<body>
<div align=center>
<H3>My Simple Twitter!!</H3>
<HR>
<form action="tweet.jsp" method="POST">
	<!-- 세션에 저장된 이름 출력 -->
	@<%=session.getAttribute("user") %> <input type="text" name="msg"><input type="submit" value="Tweet">
</form>
<HR>
<div align="left">
<UL>
<%
	// application 내장객체를 통해 msgs 이름으로 저장된 ArrayList를 가지고 옴
	ArrayList<String>msgs = (ArrayList<String>)application.getAttribute("msgs");
	
	//msgs가 null 이 아닌 경우에만 목록 출력
	if(msgs != null) {
		for(String msg : msgs) {
			out.println("<LI>"+msg+"</LI>");
		}
	}
%>
</UL>
</div>
</div>
</body>
</html>