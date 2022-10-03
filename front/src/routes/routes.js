import { BasicLayout } from "../layouts";
import { Page404, HomePage } from "../pages";

const routes = [
  {
    path: "",
    layout: BasicLayout,
    component: HomePage,
  },
  {
    path: "*",
    layout: BasicLayout,
    component: Page404,
  },
];

export default routes;
