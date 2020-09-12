<%@ page import="youngmin.bbs.ReviewbbsDAO" %>
<%@ page import="youngmin.bbs.ReviewbbsDTO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 4:04
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<% request.setCharacterEncoding("UTF-8"); %>
<html>
<head>
<%@ include file="file_header.jsp" %>

    <title>리뷰 보기</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<script>
    checkPage("${param.pageName}");
</script>
<%
    int reviewID = 0;
    if (request.getParameter("reviewID") != null)
        reviewID = Integer.parseInt(request.getParameter("reviewID"));

    ReviewbbsDTO reviewbbs = null;
    if (reviewID != 0)
    {
        reviewbbs = new ReviewbbsDAO().getBBSInfo(reviewID);
    }
%>

<div class="container">
    <div class="row">
        <table class="table table-striped" style="text-align: center;">
            <thead>
                <tr>
                    <th colspan="3" style="text-align: center">리뷰 글</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>글 제목</td>
                    <td><%= reviewbbs.getReviewTitle() %></td>
                </tr>
                <tr>
                    <td>작성자 ID</td>
                    <td><%= reviewbbs.getWriterID() %></td>
                </tr>
                <tr>
                    <td>작성일자</td>
                    <td><%= reviewbbs.getReviewDate()%></td>
                </tr>
                <tr>
                    <td>글 내용</td>
                    <td>
                        <p>
                        <%= reviewbbs.getReviewContent().replaceAll("<", "&lt;")
                                                        .replaceAll(">", "&gt;")
                                                        .replaceAll("\n", "<br/>")
                                                        .replaceAll("\"", "&quot;")
                                                        .replaceAll("&", "&amp;")%>
                        </p>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <a href="review_modify.jsp?reviewID=<%= reviewID %>" class="btn btn-primary">글 수정</a>
                        <a href="review_delete_Action.jsp?reviewID=<%= reviewID %>" class="btn btn-primary">글 삭제</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
