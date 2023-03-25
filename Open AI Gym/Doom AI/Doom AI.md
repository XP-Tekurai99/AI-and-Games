# Doom AI with ViZDoom
![image](https://user-images.githubusercontent.com/110959584/227002450-cf9466fd-b2b5-4572-9746-17dd60e48b19.png)

## Reinforcement Learning and Doom
![image](https://user-images.githubusercontent.com/110959584/227003298-3b42276f-f9f7-486e-91be-6281078a27f4.png)

### Install Libraries and Establish Environment
```
pip install vizdoom
```
### Preprocess Enivornment
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
```
pip install stable-baselines3[extra]
```

Enabling the AI to process grayscale imagery reduces the data flow which improves learning efficency. When the model sees colors, the frames are broken into three channels whereas grayscale only requires one.
* GrayScale: 240*256*1 = 61440 pixels
* Color: 240*256*3 = 184320 pixels

### Train the Model

### Test the Model

## Languages and Libraries

* Python
* vizdoom
* random
* numpy
* matplotlib

<!-- LICENSE -->
## License

Projects in this repository are distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Open AI](https://openai.com/)
* [Open AI Gym](https://github.com/openai/gym)
* [ViZDoom](https://vizdoom.cs.put.edu.pl)
* [Choose a License](https://choosealicense.com)
