import numpy as np
# Absolute collapse physics
AMBER_LIMIT = 2.0
RED_LIMIT = 3.2

def classify_health(df):
      df["Health"] = np.where(df["SII"] > RED_LIMIT, "RED",
        np.where(df["SII"] > AMBER_LIMIT, "AMBER", "GREEN")
      )
      return df
 
