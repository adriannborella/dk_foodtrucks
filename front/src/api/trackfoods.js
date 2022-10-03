import { BaseApiWithoutAuth } from "./base";

export async function trackfoodsApi(formValue) {
  return await BaseApiWithoutAuth(
    "trackfoods",
    formValue,
    "GET",
    "No se encontraron datos"
  );
}
