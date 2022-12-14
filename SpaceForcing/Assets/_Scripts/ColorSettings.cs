using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "ColorSettings", menuName = "CustomSettings/ColorSettings", order = 1)]

public class ColorSettings : ScriptableObject
{
    [Header("Cube Color Settings")]
    [SerializeField] public Color32 Hp1 = new Color32(251, 238, 223, 255);
    [SerializeField] public Color32 Hp2 = new Color32(254, 247, 100, 255);
    [SerializeField] public Color32 Hp3 = new Color32(239, 117, 191, 255);
    [SerializeField] public Color32 Hp4 = new Color32(255, 146, 44, 255);
    [SerializeField] public Color32 Hp5 = new Color32(236, 32, 79, 255);
    [SerializeField] public Color32 Hp6 = new Color32(0, 0, 0, 255);
    [SerializeField] public Color32 Hp7 = new Color32(0, 0, 0, 255);
    [SerializeField] public Color32 Hp8 = new Color32(0, 0, 0, 255);
    [SerializeField] public Color32 Hp9 = new Color32(0, 0, 0, 255);
    [SerializeField] public Color32 Hp10 = new Color32(0, 0, 0, 255);

}
