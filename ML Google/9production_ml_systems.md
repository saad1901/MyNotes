# 9. Production ML Systems

## What is a Production ML System?
- A production ML system is a deployed machine learning solution that serves predictions in real-world applications.
- It involves more than just the model: data pipelines, monitoring, deployment, and maintenance are crucial.

## Key Concepts
- **Static vs. Dynamic Training**:
  - Static: Model is trained once and deployed.
  - Dynamic: Model is retrained regularly with new data.
- **Static vs. Dynamic Inference**:
  - Static: Model uses fixed features for predictions.
  - Dynamic: Model adapts to changing input features.
- **Data Transformation**: Deciding when and where to preprocess data (before or after deployment).
- **Deployment Testing**: Ensuring the model works as expected in production.
- **Monitoring Pipelines**: Tracking data quality, model performance, and system health.
- **Questions to Ask**: What can go wrong? How will you detect and fix issues?

## Steps in Productionizing ML
1. Prepare and validate data pipelines.
2. Train and validate the model.
3. Deploy the model to production.
4. Monitor predictions and system health.
5. Update and retrain as needed.

## Example Use Cases
- Online recommendation systems.
- Fraud detection in banking.
- Real-time translation services.

---
Next: 10. Automated Machine Learning (AutoML) 