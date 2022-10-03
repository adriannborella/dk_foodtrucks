import { BASE_API } from "../utils/constants";

export async function BaseApiWithoutAuth(
  api_name,
  formValue,
  type_method = "GET",
  error_msg = "Error al conectarse"
) {
  try {
    const headers = {
      "Content-type": "application/json",
    };

    let url = `${BASE_API}/api/${api_name}/`;
    let params = {
      method: type_method,
      headers: headers,
    };

    if ("GET" === type_method) {
      url += "?" + new URLSearchParams(formValue).toString();
    } else {
      params.body = JSON.stringify(params);
    }

    const response = await fetch(url, params);

    if (response.status !== 200) {
      throw new Error(error_msg);
    }
    const result = await response.json();

    return result;
  } catch (error) {
    throw error;
  }
}
