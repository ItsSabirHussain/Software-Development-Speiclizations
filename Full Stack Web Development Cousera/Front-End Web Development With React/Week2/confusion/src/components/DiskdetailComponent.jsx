import React from "react";
import {
  Card,
  CardImg,
  CardText,
  CardBody,
  CardTitle,
  BreadcrumbItem,
  Breadcrumb
} from "reactstrap";
import { Link } from "react-router-dom";

function RenderDish({ dish }) {
  if (dish != null) {
    return (
      <div className="col-12 col-md-5 m-1">
        <Card>
          <CardImg width="100%" src={dish.image} alt={dish.name} />
          <CardBody>
            <CardTitle>{dish.name}</CardTitle>
            <CardText>{dish.description}</CardText>
          </CardBody>
        </Card>
      </div>
    );
  } else {
    return <div></div>;
  }
}

function RenderComments({ comments }) {
  if (comments == null) {
    return <div></div>;
  }
  const cmnts = comments.map(comment => {
    return (
      <dvi className="container">
        <li key={comment.id}>
          <p>{comment.comment}</p>
          <p>
            -- {comment.author}, &nbsp;
            {new Intl.DateTimeFormat("en-US", {
              year: "numeric",
              month: "long",
              day: "2-digit"
            }).format(new Date(comment.date))}
          </p>
        </li>
      </dvi>
    );
  });
  return (
    <div className="col-12 col-md-5 m-1">
      <h4> Comments </h4>
      <ul className="list-unstyled">{cmnts}</ul>
    </div>
  );
}

const DishDetail = props => {
  const dish = props.dish;
  if (dish == null) {
    return <div></div>;
  }
  const dishItem = <RenderDish dish={props.dish} />;
  const commentItem = <RenderComments comments={props.comments} />;
  return (
    <div className="container">
      <div className="row">
        <Breadcrumb>
          <BreadcrumbItem>
            <Link to="/home">Home</Link>
          </BreadcrumbItem>
          <BreadcrumbItem>
            <Link to="/menu">Menu</Link>
          </BreadcrumbItem>
          <BreadcrumbItem active>{props.dish.name} </BreadcrumbItem>
        </Breadcrumb>
        <div className="col-12">
          <h2>{props.dish.name}</h2>
          <hr></hr>
        </div>
      </div>
      <div className="row">
        {dishItem}
        {commentItem}
      </div>
    </div>
  );
};

export default DishDetail;
