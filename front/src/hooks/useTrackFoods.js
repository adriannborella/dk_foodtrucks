import { useState } from "react";
import { trackfoodsApi } from "../api/trackfoods";

export function useTrackFoods() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  const getPlaces = async (data) => {
    let response = undefined;

    try {
      setError(null);
      setLoading(true);

      response = await trackfoodsApi(data);
      setData(response);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
      throw error;
    }

    return response;
  };

  return {
    loading,
    error,
    data,
    setData,
    setLoading,
    setError,
    getPlaces,
  };
}
