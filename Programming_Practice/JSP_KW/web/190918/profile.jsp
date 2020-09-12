<%@ page import="java.util.*, java.text.*" %>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%

request.setCharacterEncoding("UTF-8");

String name = "", sex = "";
String[] hobby = new String[4];

if (request.getMethod().equals("POST"))
{
	name = request.getParameter("profile_name");
	sex = request.getParameter("sex_btn");
	hobby = request.getParameterValues("hobby_btn");
}

%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>프로필</title>
</head>
<body>
	<h2>프로필</h2>
	<hr>
	<form name=form1 method="POST">
	이름 : <input type="text" name="profile_name" width=200><br>
	성별 : <input type="radio" name="sex_btn" value="남자">남자
	<input type="radio" name="sex_btn" value="여자">여자<br>
	관심분야<br>
	<input type="checkbox" name="hobby_btn" value="게임">게임 
	<input type="checkbox" name="hobby_btn" value="스포츠">스포츠 
	<input type="checkbox" name="hobby_btn" value="영화">영화 
	<input type="checkbox" name="hobby_btn" value="여행">여행<br>
	<input type="submit" name="complete_btn" value="입력 완료">
	<input type="reset" name="reset_btn" value="재입력">
	</form>
	<hr>
	<% 
	SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.KOREA);
	Date curTime = new Date(); 
	%>
	작성시간 : <%= formatter.format(curTime) %><br>
	이름 : <%= name %><br>
	성별 : <%= sex %><br>
	관심분야 : <% for (int i = 0; i < hobby.length; i++) { %> <%= hobby[i] %> <%} %>
</body>
</html>