# -*- coding: utf-8 -*-
# @author: Kevin
# @email: 2112164129@e.gzhu.edu.cn
# @date: 2022/11/18

## test


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', type=int, default=32, help='batch size')  #required=True 必需参数
parser.add_argument('--lr_rate', type=float, default=1e-3, help='learning rate')
args = parser.parse_args()


if __name__ == '__main__':

    print('Hello github!')
    print(f'batch_size = {args.batch_size}, lr_rate = {args.lr_rate}')
