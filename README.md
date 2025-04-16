# 📈 Options Pricing Using Deep Learning

---

## 👥 The Team

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/AdamK14">
        <img src="https://github.com/AdamK14.png" width="100px;" alt="AdamK14"/><br />
        <sub><b>Adam K.</b></sub>
      </a><br />
      💻 Developer
    </td>
    <td align="center">
      <a href="https://github.com/bye37gatech">
        <img src="https://github.com/bye37gatech.png" width="100px;" alt="bye37gatech"/><br />
        <sub><b>Brandon Y.</b></sub>
      </a><br />
      💻 Developer
    </td>
    <td align="center">
      <a href="https://github.com/Jessica2268">
        <img src="https://github.com/Jessica2268.png" width="100px;" alt="Jessica2268"/><br />
        <sub><b>Jessica L.</b></sub>
      </a><br />
      📝 Presentation & Report
    </td>
    <td align="center">
      <a href="https://github.com/andyvo2004">
        <img src="https://github.com/andyvo2004.png" width="100px;" alt="andyvo2004"/><br />
        <sub><b>Andy V.</b></sub>
      </a><br />
      📝 Presentation & Report
    </td>
    <td align="center">
      <a href="https://github.com/dyu27">
        <img src="https://github.com/dyu27.png" width="100px;" alt="dyu27"/><br />
        <sub><b>Daniel Y.</b></sub>
      </a><br />
      📝 Presentation & Report
    </td>
  </tr>
</table>

> Adam and Brandon led the development of the code and model implementations. Jessica, Andy, and Daniel contributed significantly to the final presentation and research paper.

---

## 🧠 Project Summary

- **Data Source**: AAPL options data (2016–2023), combining multiple CSV files and preprocessed for model input.
- **Models Used**:
  - **LSTM**: Captures temporal patterns in time-series data.
  - **MLP1 / MLP2**: Standard and deeper feedforward neural networks.
- **Target Variables**: Predicted mid-prices of call and put options.
- **Evaluation Metric**: Mean Squared Error (MSE)

---

## 📊 Key Findings

- LSTM showed a slight performance edge due to its ability to model sequential data.
- MLP models still performed competitively, especially with well-tuned architectures.
- All models showed reasonable predictive performance, validating the use of deep learning in financial modeling.

---

## 📁 File Overview

- `lstm.ipynb` — LSTM model implementation and training
- `mlp1_calls.ipynb`, `mlp1_puts.ipynb` — MLP1 model for call and put options
- `mlp2_calls.ipynb`, `mlp2_puts.ipynb` — MLP2 model for call and put options