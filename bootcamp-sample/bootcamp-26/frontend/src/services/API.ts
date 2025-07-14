import axios from "axios";

export default axios.create({
  // baseURL: `http://localhost:8090/`

  baseURL: `http://a0aa7135489d44e0e93ded4da02cc684-1738386212.us-east-2.elb.amazonaws.com:8090/`
});
