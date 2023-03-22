# Mario AI
![image](https://user-images.githubusercontent.com/110959584/227002450-cf9466fd-b2b5-4572-9746-17dd60e48b19.png)

## Reinforcement Learning and Mario
![image](https://user-images.githubusercontent.com/110959584/227003298-3b42276f-f9f7-486e-91be-6281078a27f4.png)

### Install Libraries and Establish Environment
```
!pip install gym_super_mario_bros==7.4.0 nes_py==8.2.1
```
### Preprocess Enivornment
```
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
```
!pip install stable-baselines3[extra]
```

Enabling the AI to process grayscale imagery reduces the data flow which improves learning efficency. When the model sees colors, the frames are broken into three channels whereas grayscale only requires one.
* GrayScale: 240*256*1 = 61440 pixels
* Color: 240*256*3 = 184320 pixels

### Train the Model

### Test the Model

## Languages and Libraries

* Python
* nes-py
* gym-super-mario-bros

<!-- LICENSE -->
## License

Projects in this repository are distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Open AI](https://openai.com/)
* [Open AI Gym](https://github.com/openai/gym)
* [Super Mario Bros](https://pypi.org/project/gym-super-mario-bros/)
* [Nes-py](https://pypi.org/project/nes-py/)
* [Choose a License](https://choosealicense.com)
