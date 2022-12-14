using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "GameSettings", menuName = "CustomSettings/GameSettings", order = 0)]

public class GameSettings : ScriptableObject
{
    public float ProjectileSpeed = 10.0f;
}
