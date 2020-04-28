import React, { Component } from "react";
import { CardImgOverlay } from "reactstrap";
import { Card, CardImg, CardText, CardBody, CardTitle } from "reactstrap";

class Menu extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    console.log("Menu Component constructor is invoked.");
  }

  componentDidMount() {
    console.log("Menu Component conponentDidMount is invoked.");
  }

  renderDish(dish) {
    if (dish != null) {
      return (
        <Card>
          <CardImg width="100" object src={dish.image} alt={dish.name} />
          <CardBody>
            <CardTitle>{dish.name}</CardTitle>
            <CardText>{dish.description}</CardText>
          </CardBody>
        </Card>
      );
    } else {
      return <div></div>;
    }
  }

  state = {};

  render() {
    const menu = this.props.dishes.map(dish => {
      return (
        <div key={dish.id} className="col-12 col-md-5 m-1">
          <Card onClick={() => this.props.onClick(dish.id)}>
            <CardImg width="100" object src={dish.image} alt={dish.name} />
            <CardImgOverlay body className="ml-5">
              <CardTitle>{dish.name}</CardTitle>
            </CardImgOverlay>
          </Card>
        </div>
      );
    });

    console.log("Menu Component render is invoked.");

    return (
      <div className="container">
        <div className="row">{menu}</div>
      </div>
    );
  }
}

export default Menu;
