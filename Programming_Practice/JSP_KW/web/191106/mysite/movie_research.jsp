<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 1:26
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp" %>
    <script src="../../js/page_func.js"></script>

    <title>영화 검색</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<script>checkPage("${param.pageName}")</script>

<div class="container-fluid">
    <form method="GET" action="movie_research_result.jsp">
        <div class="form-group">
            <label for="input_research_movie_name">검색 : </label>
                <input type="text" id="input_research_movie_name" name="input_research" placeholder="영화 제목 입력" maxlength="60"/>
            <input type="submit" value="검색"/>
        </div>
    </form>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
