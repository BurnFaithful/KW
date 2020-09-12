<%@ page import="youngmin.api.MovieAPI" %>
<%@ page import="youngmin.api.MovieInfoJO" %>
<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-20
  Time: 오후 3:19
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp"%>
    <title>Title</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<%
    MovieAPI movieAPI = new MovieAPI();

    String movieDataJson = movieAPI.getJson(request.getParameter("input_research"));
//    out.println(movieDataJson);

    MovieInfoJO movieInfoObj = movieAPI.parseJsonToObject(movieDataJson);
%>
    <div class="container">
        <table class="table table-bordered">
            <thead>
                <th>영화 타이틀</th>
                <th>영화 포스터</th>
                <th>영화정보 링크</th>
            </thead>
            <tbody>
            <%
                for (int i = 0; i < movieInfoObj.getItems().length; ++i)
                {
            %>
                <tr>
                    <td><%= movieInfoObj.getItems()[i].getTitle()%></td>
                    <td><img src="<%= movieInfoObj.getItems()[i].getImage()%>" alt=""></td>
                    <td><a href="<%= movieInfoObj.getItems()[i].getLink()%>"><%= movieInfoObj.getItems()[i].getTitle()%></a></td>
                </tr>
            <%
                }
            %>
            </tbody>
        </table>
    </div>

<%@include file="page_footer.jsp" %>
</body>
</html>
