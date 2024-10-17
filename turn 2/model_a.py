import unittest
import pandas as pd
import matplotlib.pyplot as plt


class TestDataVisualizationComponents(unittest.TestCase):

    def test_validate_bar_chart_creation(self):
        # Dummy data for testing
        data = {
            'Product': ['Laptop', 'Mobile', 'Tablet', 'Desktop'],
            'Sales': [1000, 500, 300, 800]
        }
        df = pd.DataFrame(data)

        # Function to create the bar chart
        def create_bar_chart(df, x, y):
            ax = df.plot(kind='bar', x=x, y=y, figsize=(10, 6))
            plt.title('Sales by Product')
            plt.xlabel('Product')
            plt.ylabel('Sales')
            return ax

        # Create the bar chart
        ax = create_bar_chart(df, x='Product', y='Sales')

        # Check if the chart is created successfully
        self.assertIsNotNone(ax)

        # Check if the chart has the correct title
        self.assertEqual(ax.get_title(), 'Sales by Product')

        # Check if the chart has the correct x-axis label
        self.assertEqual(ax.get_xlabel(), 'Product')

        # Check if the chart has the correct y-axis label
        self.assertEqual(ax.get_ylabel(), 'Sales')


if __name__ == '__main__':
    unittest.main()
