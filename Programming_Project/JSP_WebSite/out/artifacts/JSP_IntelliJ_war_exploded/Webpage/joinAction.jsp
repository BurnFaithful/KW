<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ page import="youngmin.web.UserDAO, java.io.PrintWriter" %>
<% request.setCharacterEncoding("UTF-8"); %>
<jsp:useBean id="user" class="youngmin.web.User" scope="page" />
<jsp:setProperty name="user" property="id" />
<jsp:setProperty name="user" property="password" />
<jsp:setProperty name="user" property="name" />
<jsp:setProperty name="user" property="age" />
<jsp:setProperty name="user" property="email" />
<jsp:setProperty name="user" property="phoneNumber" />

<%
	PrintWriter script = response.getWriter();

	if (user.getId() == null || user.getPassword() == null ||
			user.getName() == null || user.getAge() == 0 ||
			user.getEmail() == null || user.getPhoneNumber() == null)
	{
		script.println("<script>");
		script.println("alert('입력이 되지 않은 사항이 있습니다.')");
		script.println("history.back()");
		script.println("</script>");
	}
	else
	{
		UserDAO DAO = new UserDAO();
		int result = DAO.join(user);
		if (result == -1)
		{
			script.println("<script>");
			script.println("alert('이미 존재하는 아이디입니다.')");
			script.println("history.back()");
			script.println("</script>");
		}
		else
		{
			script.println("<script>");
			script.println("location.href='main.jsp'");
			script.println("</script>");
		}
	}

%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	
</body>
</html>