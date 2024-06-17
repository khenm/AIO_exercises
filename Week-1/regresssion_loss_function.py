import random
import math


def regression_loss_function():
    """Calculate loss based on the regression loss function,
    namely MAE, MSE, RMSE.
    Inputs:
        num_samples: number of samples created
        loss_name: loss function 
    """

    # input
    num_samples = input(
        'Input number of samples (integer number) which are generated: ')
    loss_name: str = input('Input loss name: ')
    # num_samples condition
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    num_samples = int(num_samples)

    # MAE function
    if loss_name == 'MAE':
        final_loss: float = 0
        for i in range(num_samples):
            # creating random predict and target
            predict_mae_x: float = random.uniform(0, 10)
            target_mae_x: float = random.uniform(0, 10)
            # loss
            loss: float = abs(target_mae_x - predict_mae_x)
            final_loss += loss
            # display each sample result
            print(f'loss name: {loss_name}, sample: {i}, \
                  pred: {predict_mae_x}, target: {target_mae_x}, loss: {loss}')
        # calculate MAE final loss by dividing it by number of samples
        final_loss /= num_samples
        # print final loss
        print(f'final {loss_name}: {final_loss}')

    # MSE function
    if loss_name == 'MSE':
        final_loss: float = 0
        for i in range(num_samples):
            # creating random predict and target
            predict_mse_x: float = random.uniform(0, 10)
            target_mse_x: float = random.uniform(0, 10)

            # loss
            loss: float = math.pow((target_mse_x - predict_mse_x), 2)
            final_loss += loss

            # display each sample result
            print(f'loss name: {loss_name}, sample: {i}, \
                  pred: {predict_mse_x}, target: {target_mse_x}, loss: {loss}')
        # calculate MSE final loss by dividing it by number of samples
        final_loss /= num_samples
        # print final loss
        print(f'final {loss_name}: {final_loss}')

    # RMSE function
    if loss_name == 'RMSE':
        final_loss: float = 0
        for i in range(num_samples):
            # creating random predict and target
            predict_rmse_x: float = random.uniform(0, 10)
            target_rmse_x: float = random.uniform(0, 10)

            # loss
            loss: float = math.pow((target_rmse_x - predict_rmse_x), 2)
            final_loss += loss

            # display each sample result
            print(f'loss name: {loss_name}, sample: {i}, \
                  pred: {predict_rmse_x}, target: {target_rmse_x}, loss: {loss}')
        # calculate RMSE final loss by dividing it by number of samples
        final_loss /= num_samples
        # and take square root
        final_loss = math.sqrt(final_loss)
        # print final loss
        print(f'final {loss_name}: {final_loss}')


def main():
    regression_loss_function()


if __name__ == "__main__":
    main()
